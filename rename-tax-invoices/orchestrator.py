"""
오케스트라 패턴 파일명 자동 변환 도구

파일 유형 판별 후 처리기 배분:
  텍스트 PDF (세금계산서/거래명세서) → PyMuPDF 처리기
  이미지 PDF / 이미지 파일 (영수증)  → Gemini Vision 처리기
"""

import os
import sys
import shutil
from pathlib import Path

import fitz

from handlers.pymupdf_handler import detect_type, process_pdf
from handlers.gemini_handler import process_receipt

PDF_DIR = Path(__file__).parent / "pdf"
ENV_FILE = Path(__file__).parent / ".env"

DEST_SALES   = Path(r"C:\Users\yujin\OneDrive\Desktop\박유진\1. 매출서류")
DEST_FINANCE = Path(r"C:\Users\yujin\OneDrive\Desktop\박유진\0-1. 재무관리")

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
MIN_TEXT_CHARS = 50


def _dest_folder(file_type: str, new_name: str) -> Path:
    """파일 유형과 파일명(YYYYMMDD로 시작)에서 월별 목적 폴더를 반환."""
    year, month = new_name[:4], new_name[4:6]
    folder_name = f"{year}-{month}" if year.isdigit() and month.isdigit() else "날짜미상"
    base = DEST_SALES if file_type in ("세금계산서", "거래명세서") else DEST_FINANCE
    return base / folder_name


# ── API 키 로드 ────────────────────────────────────────────────────────

def _load_api_key():
    if os.environ.get("GEMINI_API_KEY"):
        return

    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("GEMINI_API_KEY="):
                os.environ["GEMINI_API_KEY"] = line.split("=", 1)[1].strip()
                return

    print("\nGemini API 키가 필요합니다 (이미지/영수증 처리용).")
    key = input("GEMINI_API_KEY: ").strip()
    if not key:
        print("API 키 없이는 이미지/영수증을 처리할 수 없습니다.")
        return

    os.environ["GEMINI_API_KEY"] = key
    save = input("이 키를 저장해서 다음부터 자동 입력할까요? (y/n): ").strip().lower()
    if save == "y":
        with open(ENV_FILE, "w", encoding="utf-8") as f:
            f.write(f"GEMINI_API_KEY={key}\n")
        print(f"저장 완료: {ENV_FILE}")


# ── 파일 분류 ──────────────────────────────────────────────────────────

def _classify(file_path: Path) -> tuple[str, list | None]:
    ext = file_path.suffix.lower()

    if ext in IMAGE_EXTS:
        return "영수증", None

    if ext == ".pdf":
        doc = fitz.open(str(file_path))
        text = doc[0].get_text()
        doc.close()

        if len(text.strip()) >= MIN_TEXT_CHARS:
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            doc_type = detect_type(lines)
            if doc_type:
                return doc_type, lines

        return "영수증", None

    return "미지원", None


# ── 메인 ──────────────────────────────────────────────────────────────

def run():
    if not PDF_DIR.exists():
        print(f"오류: '{PDF_DIR}' 폴더가 없습니다.")
        sys.exit(1)

    files: list[Path] = []
    for pattern in ["*.[Pp][Dd][Ff]", "*.jpg", "*.jpeg", "*.png",
                    "*.JPG", "*.JPEG", "*.PNG", "*.gif", "*.webp"]:
        files.extend(PDF_DIR.glob(pattern))
    files = sorted(set(files))

    if not files:
        print(f"처리할 파일이 없습니다. '{PDF_DIR}' 폴더를 확인해주세요.")
        return

    # 이미지/영수증이 있을 때만 API 키 로드
    needs_gemini = any(
        _classify(f)[0] == "영수증"
        for f in files
        if f.suffix.lower() in IMAGE_EXTS
        or (f.suffix.lower() == ".pdf")
    )
    if needs_gemini:
        _load_api_key()

    print(f"\n{len(files)}개 파일 분석 중...")

    results = []
    for file_path in files:
        try:
            file_type, lines = _classify(file_path)

            if file_type in ("세금계산서", "거래명세서"):
                new_name = process_pdf(file_path, file_type, lines)
                results.append((file_path, file_type, new_name, None))

            elif file_type == "영수증":
                new_name = process_receipt(file_path)
                results.append((file_path, "영수증(Gemini)", new_name, None))

            else:
                results.append((file_path, "미지원", None, None))

        except Exception as e:
            results.append((file_path, "오류", None, str(e)))

    print("\n[ 변환 미리보기 ]")
    print("-" * 90)
    for file_path, file_type, new_name, error in results:
        if error:
            print(f"[오류]   {file_path.name}")
            print(f"         {error}")
        elif new_name is None:
            print(f"[{file_type}] {file_path.name}: 처리 불가")
        else:
            dest = _dest_folder(file_type, new_name) / new_name
            print(f"[{file_type}] {file_path.name}")
            print(f"  → {dest}")
    print("-" * 90)

    answer = input("\n위 경로로 이동할까요? (y/n): ").strip().lower()
    if answer != "y":
        print("취소했습니다.")
        return

    for file_path, file_type, new_name, error in results:
        if error or new_name is None:
            print(f"건너뜀: {file_path.name}")
            continue
        dest_dir = _dest_folder(file_type, new_name)
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / new_name
        if dest.exists():
            print(f"이미 존재하여 건너뜀: {new_name}")
            continue
        shutil.move(str(file_path), str(dest))
        print(f"완료: {file_path.name} → {dest}")

    print("\n모든 작업이 완료되었습니다.")


if __name__ == "__main__":
    run()
