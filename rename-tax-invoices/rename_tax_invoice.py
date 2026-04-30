import fitz
import re
from pathlib import Path

PDF_DIR = r"C:\Users\yujin\OneDrive\Desktop\claude\rename-tax-invoices\pdf"

SKIP_KEYWORDS = {"합계금액", "현금", "수표", "어음", "외상", "비고", "수정사유", "총합계"}


# ── 공통 ──────────────────────────────────────────────────────────────

def get_lines(pdf_path):
    doc = fitz.open(pdf_path)
    lines = [l.strip() for l in doc[0].get_text().splitlines()]
    return [l for l in lines if l]


def detect_type(lines):
    joined = "\n".join(lines)
    if "전자세금계산서" in joined:
        return "세금계산서"
    if "거래명세서" in joined:
        return "거래명세서"
    return None


def sanitize(s):
    return re.sub(r'[\\/:*?"<>|]', "", s).strip()


# ── 세금계산서 ─────────────────────────────────────────────────────────

def extract_tax_invoice(lines):
    # 날짜: 4자리 연도 이후 월/일
    date_str = None
    for i, line in enumerate(lines):
        if re.match(r"^\d{4}$", line) and i + 2 < len(lines):
            month = lines[i + 1].zfill(2)
            day = lines[i + 2].zfill(2)
            if re.match(r"^\d{1,2}$", month) and re.match(r"^\d{1,2}$", day):
                date_str = f"{line}{month}{day}"
                break

    # 공급받는자: "(법인명) 회사명" 두 번째 등장
    matches = re.findall(r"\(법인명\)\s*(.+)", "\n".join(lines))
    recipient = matches[1].strip() if len(matches) >= 2 else (matches[0].strip() if matches else None)

    # 품목: 품목 테이블의 첫 번째 항목
    item = None
    for i, line in enumerate(lines):
        if re.match(r"^\d{2}$", line) and i + 1 < len(lines):
            nxt = lines[i + 1]
            # 케이스 1: "09 품목명..." (일+품목 같은 줄)
            m = re.match(r"^\d{2}\s+(.+)", nxt)
            if m:
                item = m.group(1).strip()
                if i + 2 < len(lines):
                    cont = lines[i + 2]
                    if not re.match(r"^[\d,]+$", cont) and cont not in SKIP_KEYWORDS:
                        item += " " + cont
                break
            # 케이스 2: "09" 단독, 다음 줄에 품목
            if re.match(r"^\d{2}$", nxt) and i + 2 < len(lines):
                candidate = lines[i + 2]
                if not re.match(r"^[\d,]+$", candidate) and candidate not in SKIP_KEYWORDS:
                    item = candidate.strip()
                    if i + 3 < len(lines):
                        cont = lines[i + 3]
                        if not re.match(r"^[\d,]+$", cont) and cont not in SKIP_KEYWORDS:
                            item += " " + cont
                    break

    return date_str, recipient, item


def make_tax_invoice_name(date_str, recipient, item):
    date_part = date_str or "날짜미상"
    r = sanitize(recipient) if recipient else "거래처미상"
    it = sanitize(item) if item else "품목미상"
    return f"{date_part} 세금계산서({r} - {it}).pdf"


# ── 거래명세서 ─────────────────────────────────────────────────────────

def extract_receipt(lines):
    # 거래일자: "거래일자" 다음 줄 "YYYY/MM/DD"
    date_str = None
    for i, line in enumerate(lines):
        if line == "거래일자" and i + 1 < len(lines):
            m = re.match(r"(\d{4})/(\d{2})/(\d{2})", lines[i + 1])
            if m:
                date_str = m.group(1) + m.group(2) + m.group(3)
                break

    # 거래처명: "거래처명" 다음 줄
    recipient = None
    for i, line in enumerate(lines):
        if line == "거래처명" and i + 1 < len(lines):
            recipient = lines[i + 1].strip()
            break

    # 적요: 첫 번째 품목 행의 "부가세금액 적요내용" 패턴에서 추출
    # 품목 행 패턴: "MM/DD 품목명"
    item_joyo = None
    for i, line in enumerate(lines):
        if re.match(r"^\d{2}/\d{2}\s+.+", line):
            # 이후 줄에서 "숫자, 적요" 형태 탐색
            for j in range(i + 1, min(i + 6, len(lines))):
                m = re.match(r"^[\d,]+\s+(.+)", lines[j])
                if m:
                    joyo = m.group(1).strip()
                    # 다음 줄이 이어지는 내용이면 합치기
                    if j + 1 < len(lines):
                        cont = lines[j + 1]
                        if not re.match(r"^[\d,]+$", cont) and cont not in SKIP_KEYWORDS and not re.match(r"^\d{2}/\d{2}", cont):
                            joyo += cont
                    item_joyo = joyo
                    break
            break

    return date_str, recipient, item_joyo


def make_receipt_name(date_str, recipient, joyo):
    date_part = date_str or "날짜미상"
    r = sanitize(recipient) if recipient else "거래처미상"
    j = sanitize(joyo) if joyo else "적요미상"
    return f"{date_part} 거래명세서({r} {j}).pdf"


# ── 메인 ──────────────────────────────────────────────────────────────

def process_pdf(pdf_path):
    lines = get_lines(pdf_path)
    doc_type = detect_type(lines)

    if doc_type == "세금계산서":
        date_str, recipient, item = extract_tax_invoice(lines)
        return doc_type, make_tax_invoice_name(date_str, recipient, item)
    elif doc_type == "거래명세서":
        date_str, recipient, joyo = extract_receipt(lines)
        return doc_type, make_receipt_name(date_str, recipient, joyo)
    else:
        return "미확인", None


def run():
    pdf_dir = Path(PDF_DIR)
    files = sorted(pdf_dir.glob("*.[Pp][Dd][Ff]"))

    results = []
    for pdf_file in files:
        try:
            doc_type, new_name = process_pdf(str(pdf_file))
            results.append((pdf_file, doc_type, new_name, None))
        except Exception as e:
            results.append((pdf_file, "오류", None, str(e)))

    print("\n[ 변환 미리보기 ]")
    print("-" * 90)
    for pdf_file, doc_type, new_name, error in results:
        if error:
            print(f"[오류] {pdf_file.name}: {error}")
        elif new_name is None:
            print(f"[미확인] {pdf_file.name}: 문서 종류를 인식하지 못했습니다.")
        else:
            print(f"[{doc_type}] {pdf_file.name}")
            print(f"  → {new_name}")
    print("-" * 90)

    answer = input("\n위 이름으로 변경할까요? (y/n): ").strip().lower()
    if answer != "y":
        print("취소했습니다.")
        return

    for pdf_file, doc_type, new_name, error in results:
        if error or new_name is None:
            print(f"건너뜀: {pdf_file.name}")
            continue
        new_path = pdf_file.parent / new_name
        if new_path.exists():
            print(f"이미 존재하여 건너뜀: {new_name}")
            continue
        pdf_file.rename(new_path)
        print(f"완료: {pdf_file.name} → {new_name}")

    print("\n모든 작업이 완료되었습니다.")


if __name__ == "__main__":
    run()
