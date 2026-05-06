import os
import re
import base64
import json
from pathlib import Path

import fitz
from google import genai
from google.genai import types

GEMINI_MODEL = "gemini-2.0-flash-lite"

MIME_MAP = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}

PROMPT = """
이 영수증 이미지나 문서에서 결제 날짜와 총 금액을 추출하세요.
형식 요구사항:
1. date: YYYYMMDD 형식 (예: 2024-04-29 → 20240429)
2. amount: 천 단위 쉼표가 포함된 총 결제 금액 (예: 15000 → 15,000)
"""


def _get_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY 환경변수를 설정해주세요.\n"
            "예) set GEMINI_API_KEY=your_api_key_here"
        )
    return genai.Client(api_key=api_key)


def _to_base64(file_path: Path) -> tuple[str, str]:
    """Returns (base64_string, mime_type). PDF is rendered to JPEG first."""
    ext = file_path.suffix.lower()
    if ext == ".pdf":
        doc = fitz.open(str(file_path))
        pix = doc[0].get_pixmap(matrix=fitz.Matrix(2, 2))
        img_bytes = pix.tobytes("jpeg")
        doc.close()
        return base64.b64encode(img_bytes).decode(), "image/jpeg"

    mime_type = MIME_MAP.get(ext, "image/jpeg")
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode(), mime_type


def _extract(file_path: Path) -> dict:
    client = _get_client()
    b64_data, mime_type = _to_base64(file_path)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=[{
            "parts": [
                {"inline_data": {"mime_type": mime_type, "data": b64_data}},
                {"text": PROMPT},
            ]
        }],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "YYYYMMDD 형식의 날짜"},
                    "amount": {"type": "string", "description": "쉼표 포함 총 금액"},
                },
                "required": ["date", "amount"],
            },
        ),
    )

    result = json.loads(response.text)

    # Normalize date → YYYYMMDD
    date_str = re.sub(r"[^0-9]", "", result["date"])
    if len(date_str) == 6:          # YYMMDD → YYYYMMDD
        date_str = "20" + date_str
    elif len(date_str) > 8:
        date_str = date_str[:8]

    # Normalize amount → comma-separated
    amount_digits = re.sub(r"[^0-9]", "", result["amount"])
    amount_str = f"{int(amount_digits):,}" if amount_digits else result["amount"]

    return {"date": date_str, "amount": amount_str}


def sanitize(s: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "", s).strip()


def process_receipt(file_path: Path) -> str:
    try:
        data = _extract(file_path)
    except Exception as e:
        msg = str(e)
        if "429" in msg or "RESOURCE_EXHAUSTED" in msg:
            raise RuntimeError("Gemini API 할당량 초과 (무료 티어 한도). 잠시 후 다시 시도하거나 API 결제를 활성화하세요.")
        if "API_KEY" in msg or "401" in msg or "403" in msg:
            raise RuntimeError("Gemini API 키가 올바르지 않습니다.")
        raise RuntimeError(f"Gemini 처리 실패: {msg[:120]}")
    date_part = data.get("date") or "날짜미상"
    amount_part = sanitize(data.get("amount", "금액미상"))
    ext = file_path.suffix.lower()
    return f"{date_part} 영수증({amount_part}원){ext}"
