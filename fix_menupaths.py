with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

replacements = [
    # ── 프로그램 설정 ─────────────────────────────────────────────
    # sec-basic-master (기본 마스터 관리) — 2곳
    ('메뉴 > 코드메뉴 > <span>기본 마스터 관리</span>',
     '메뉴 > 프로그램 설정 > <span>기본 마스터 관리</span>'),
    # sec-equipment (장비) — 마스터 구분 변경 포함
    ('메뉴 > 코드 메뉴 > <span>기본 마스터 관리</span> → 마스터 구분 \'장비\'로 변경',
     '메뉴 > 프로그램 설정 > <span>기본 마스터 관리</span> → 마스터 구분 \'장비\'로 변경'),
    # sec-material (검사실별 물질 관리)
    ('메뉴 > 코드 메뉴 > <span>검사실별 Control 관리</span>',
     '메뉴 > 프로그램 설정 > <span>검사실별 물질 관리</span>'),

    # ── 정도관리 설정 ─────────────────────────────────────────────
    # sec-test-item (검사항목)
    ('메뉴 > 코드 메뉴 > <span>검사실별 검사 관리</span>',
     '메뉴 > 정도관리 설정 > <span>검사항목</span>'),
    # sec-qc-lot (QC LOT)
    ('메뉴 > 코드메뉴 > <span>QC 마스터 통합관리</span>',
     '메뉴 > 정도관리 설정 > <span>QC LOT</span>'),
    # sec-reagent (시약)
    ('메뉴 > 코드 메뉴 > <span>검사실별 시약 관리</span>',
     '메뉴 > 정도관리 설정 > <span>Reagent LOT</span>'),
    # sec-reagent-lot (시약 LOT)
    ('메뉴 > 코드메뉴 > <span>시약 마스터 통합관리</span>',
     '메뉴 > 정도관리 설정 > <span>Reagent LOT</span>'),
    # sec-allowable (Target/허용범위)
    ('메뉴 > 코드메뉴 > <span>허용범위 설정 관리</span>',
     '메뉴 > 정도관리 설정 > <span>Target/허용범위</span>'),

    # ── 홈 ────────────────────────────────────────────────────────
    # sec-dashboard
    ('메뉴 > 결과관리 > <span>대시보드</span>',
     '메뉴 > 홈 > <span>대시보드</span>'),
    # sec-qc-result
    ('메뉴 > 코드 메뉴 > <span>QC 결과 확인</span>',
     '메뉴 > 홈 > <span>QC 결과 확인</span>'),
    # sec-data-query
    ('메뉴 > 조회 > <span>QC 데이터 조회</span> → 데이터 조회 구간을 LOT의 시작일자, 종료일자로 변경',
     '메뉴 > 홈 > <span>QC 데이터 조회</span> → 데이터 조회 구간을 LOT의 시작일자, 종료일자로 변경'),
    ('메뉴 > 조회 > <span>QC 데이터 조회</span>',
     '메뉴 > 홈 > <span>QC 데이터 조회</span>'),
    # sec-barcode
    ('메뉴 > 결과관리 > <span>Barcode 출력</span>',
     '메뉴 > 홈 > <span>바코드 출력</span>'),

    # ── Rule Refresh (정도관리 설정 > QC LOT) ─────────────────────
    ('메뉴 > 코드관리 > <span>QC 마스터 통합관리</span> → LOT 타깃값을 수정',
     '메뉴 > 정도관리 설정 > <span>QC LOT</span> → LOT 타깃값을 수정'),

    # ── 보고서 ────────────────────────────────────────────────────
    ('메뉴 > 조회 > <span>QC Report</span>',
     '메뉴 > 보고서 > <span>허용범위 보고서</span>'),
    ('메뉴 > 조회 > <span>CV Report</span>',
     '메뉴 > 보고서 > <span>CV Report</span>'),
    ('메뉴 > 조회 > <span>Qualitative Report</span>',
     '메뉴 > 보고서 > <span>정성 보고서</span>'),

    # ── 장비간 상관성 평가 ────────────────────────────────────────
    ('메뉴 > 조회 > <span>장비간 상관성 조회</span>',
     '메뉴 > <span>장비간 상관성 평가</span>'),

    # ── 환자 결과 확인 ────────────────────────────────────────────
    ('메뉴 > AgentQC Extended > <span>환자 결과 조회</span>',
     '메뉴 > <span>환자 결과 확인</span>'),
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
        print(f'OK: {old[:50]}...')
    else:
        print(f'MISS: {old[:60]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done.')
