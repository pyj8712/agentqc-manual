with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Replace nav block ─────────────────────────────────────
old_nav = """  <div id="nav">
    <div class="nav-group-label">시작하기</div>
    <div class="nav-item active" data-target="sec-intro">
      <span class="nav-step">―</span> 사전 안내
    </div>

    <div class="nav-group-label">STEP 01</div>
    <div class="nav-item" data-target="sec-user-create">
      <span class="nav-step">01</span> 사용자 계정 만들기
    </div>
    <div class="nav-item" data-target="sec-password">
      <span class="nav-step">01</span> 비밀번호 변경하기
    </div>

    <div class="nav-group-label">STEP 02</div>
    <div class="nav-item" data-target="sec-basic-master">
      <span class="nav-step">02</span> 기본 마스터 관리
    </div>
    <div class="nav-item" data-target="sec-equipment">
      <span class="nav-step">02</span> 마스터 코드 — 장비
    </div>
    <div class="nav-item" data-target="sec-test-item">
      <span class="nav-step">02</span> 마스터 코드 — 검사항목
    </div>
    <div class="nav-item" data-target="sec-material">
      <span class="nav-step">02</span> 마스터 코드 — 물질
    </div>
    <div class="nav-item" data-target="sec-qc-lot">
      <span class="nav-step">02</span> 마스터 코드 — QC LOT
    </div>
    <div class="nav-item" data-target="sec-lot-faq">
      <span class="nav-step">02</span> LOT FAQ
    </div>
    <div class="nav-item" data-target="sec-reagent">
      <span class="nav-step">02</span> 마스터 코드 — 시약
    </div>
    <div class="nav-item" data-target="sec-reagent-lot">
      <span class="nav-step">02</span> 마스터 코드 — 시약 LOT
    </div>
    <div class="nav-item" data-target="sec-allowable">
      <span class="nav-step">02</span> 허용범위 설정 관리
    </div>

    <div class="nav-group-label">STEP 03</div>
    <div class="nav-item" data-target="sec-dashboard">
      <span class="nav-step">03</span> 대시보드 화면 구성
    </div>
    <div class="nav-item" data-target="sec-dashboard-basic">
      <span class="nav-step">03</span> 대시보드 기본 사용법
    </div>

    <div class="nav-item" data-target="sec-qc-result">
      <span class="nav-step">03</span> QC 결과 확인
    </div>

    <div class="nav-group-label">STEP 04</div>
    <div class="nav-item" data-target="sec-data-query">
      <span class="nav-step">04</span> QC 데이터 조회
    </div>
    <div class="nav-item" data-target="sec-rule-refresh">
      <span class="nav-step">04</span> Rule Refresh
    </div>

    <div class="nav-group-label">STEP 05</div>
    <div class="nav-item" data-target="sec-reports">
      <span class="nav-step">05</span> 보고서 출력
    </div>

    <div class="nav-group-label">STEP 06</div>
    <div class="nav-item" data-target="sec-extended">
      <span class="nav-step">06</span> Extended 기능
    </div>
    <div class="nav-item" data-target="sec-barcode">
      <span class="nav-step">06</span> Barcode 기능
    </div>
  </div>"""

new_nav = """  <div id="nav">
    <div class="nav-group-label">시작하기</div>
    <div class="nav-item active" data-target="sec-intro">
      <span class="nav-step">―</span> 사전 안내
    </div>

    <div class="nav-group-label">STEP 01 홈</div>
    <div class="nav-item" data-target="sec-qc-result">
      <span class="nav-step">01</span> QC 결과 확인
    </div>
    <div class="nav-item" data-target="sec-dashboard">
      <span class="nav-step">01</span> 대시보드
    </div>
    <div class="nav-item" data-target="sec-dashboard-basic">
      <span class="nav-step">01</span> 대시보드 기본 사용법
    </div>
    <div class="nav-item" data-target="sec-barcode">
      <span class="nav-step">01</span> 바코드 출력
    </div>
    <div class="nav-item" data-target="sec-data-query">
      <span class="nav-step">01</span> QC 데이터 조회
    </div>
    <div class="nav-item" data-target="sec-rule-refresh">
      <span class="nav-step">01</span> Rule Refresh
    </div>

    <div class="nav-group-label">STEP 02 환자 결과 확인</div>
    <div class="nav-item" data-target="sec-patient">
      <span class="nav-step">02</span> 환자 결과 확인
    </div>

    <div class="nav-group-label">STEP 03 X-Bar</div>
    <div class="nav-item" data-target="sec-xbar">
      <span class="nav-step">03</span> X-Bar 차트
    </div>
    <div class="nav-item" data-target="sec-xbar">
      <span class="nav-step">03</span> X-Bar 설정
    </div>

    <div class="nav-group-label">STEP 04 장비간 상관성 평가</div>
    <div class="nav-item" data-target="sec-correlation">
      <span class="nav-step">04</span> 장비간 상관성 평가
    </div>

    <div class="nav-group-label">STEP 05 보고서</div>
    <div class="nav-item" data-target="sec-reports">
      <span class="nav-step">05</span> 허용범위 보고서
    </div>
    <div class="nav-item" data-target="sec-reports">
      <span class="nav-step">05</span> CV Report
    </div>
    <div class="nav-item" data-target="sec-reports">
      <span class="nav-step">05</span> 정성 보고서
    </div>
    <div class="nav-item" data-target="sec-reports">
      <span class="nav-step">05</span> 보고서 통합 조회
    </div>

    <div class="nav-group-label">STEP 06 정도관리 설정</div>
    <div class="nav-item" data-target="sec-test-item">
      <span class="nav-step">06</span> 검사항목
    </div>
    <div class="nav-item" data-target="sec-qc-lot">
      <span class="nav-step">06</span> QC LOT
    </div>
    <div class="nav-item" data-target="sec-lot-faq">
      <span class="nav-step">06</span> LOT FAQ
    </div>
    <div class="nav-item" data-target="sec-allowable">
      <span class="nav-step">06</span> Target/허용범위
    </div>
    <div class="nav-item" data-target="sec-reagent">
      <span class="nav-step">06</span> Reagent
    </div>
    <div class="nav-item" data-target="sec-reagent-lot">
      <span class="nav-step">06</span> Reagent LOT
    </div>

    <div class="nav-group-label">STEP 07 프로그램 설정</div>
    <div class="nav-item" data-target="sec-basic-master">
      <span class="nav-step">07</span> 기본 마스터 관리
    </div>
    <div class="nav-item" data-target="sec-material">
      <span class="nav-step">07</span> 검사실별 물질 관리
    </div>
    <div class="nav-item" data-target="sec-equipment">
      <span class="nav-step">07</span> 장비 마스터
    </div>

    <div class="nav-group-label">STEP 08 로그인</div>
    <div class="nav-item" data-target="sec-user-create">
      <span class="nav-step">08</span> 사용자 계정 만들기
    </div>
    <div class="nav-item" data-target="sec-password">
      <span class="nav-step">08</span> 비밀번호 변경하기
    </div>
  </div>"""

if old_nav not in content:
    print("ERROR: old_nav not found"); exit(1)
content = content.replace(old_nav, new_nav)
print("1/5 Nav replaced OK")

# ── 2. Update sec-reports chapter header ──────────────────────
old_rh = """  <div class="chapter-header">
    <h1>보고서 출력</h1>
    <p>STEP 05 — QC Report / CV Report / Qualitative Report / 장비간 상관성</p>
    <p class="intro-text">카이저랩은 검사실의 인증·사사를 위해 노력하고 있어요.</p>
  </div>"""
new_rh = """  <div class="chapter-header">
    <h1>보고서</h1>
    <p>STEP 05 — 허용범위 보고서 / CV Report / 정성 보고서 / 보고서 통합 조회</p>
    <p class="intro-text">카이저랩은 검사실의 인증·사사를 위해 노력하고 있어요.</p>
  </div>"""
if old_rh not in content:
    print("ERROR: reports header not found"); exit(1)
content = content.replace(old_rh, new_rh)
print("2/5 reports header OK")

# ── 3. Split correlation out of sec-reports ───────────────────
old_corr = """
  <h2 class="section-title" style="margin-top:22px;">장비간 상관성 조회</h2>
  <div class="menu-path">메뉴 > 조회 > <span>장비간 상관성 조회</span></div>
  <p style="font-size:13px; color:var(--gray); margin-bottom:10px;">
    같은 검사를 진행하는 여러 장비가 서로 비슷한 결과를 내고 있는지 확인하기 위한 화면이에요.<br>
    기준 장비 1대와 최대 3대까지 한 번에 비교할 수 있어요.
  </p>
  <div class="two-col">
    <div class="field-box">
      <div class="field-title">비교 조건 (2가지)</div>
      <div style="font-size:12.5px; line-height:1.9; color:var(--gray); padding-top:4px;">
        <strong>A.</strong> [기준 장비]와 동일한 [결과일자 + 일련번호]로 매칭<br>
        = 정확히 '같은 조건에서 한 번에 비교'<br><br>
        <strong>B.</strong> [결과일자] 무시 후 결과일자로 정렬 후 매칭<br>
        = 정확히 같은 시점은 아니지만, 측정된 순서 기준으로 매칭
      </div>
    </div>
    <div>
      <h3 class="sub-title">계산 검증</h3>
      <p style="font-size:12.5px; color:var(--gray);">계산 검증 버튼을 누르면 통계 계산 검증창이 나오며, 검증을 화면에서 확인할 수 있어요.</p>
    </div>
  </div>
</div>
</section>

<!-- ─────────────────────────────────────────
     섹션: Extended 기능
───────────────────────────────────────── -->
<section class="section" id="sec-extended">"""

new_corr = """
</div>
</section>

<!-- ─────────────────────────────────────────
     섹션: 장비간 상관성 평가
───────────────────────────────────────── -->
<section class="section" id="sec-correlation">
<div class="page">
  <div class="chapter-header">
    <h1>장비간 상관성 평가</h1>
    <p>STEP 04 — 장비간 상관성 조회</p>
    <p class="intro-text">같은 검사를 진행하는 여러 장비가 서로 비슷한 결과를 내고 있는지 확인하는 기능이에요.</p>
  </div>

  <h2 class="section-title">장비간 상관성 조회</h2>
  <div class="menu-path">메뉴 > 조회 > <span>장비간 상관성 조회</span></div>
  <p style="font-size:13px; color:var(--gray); margin-bottom:10px;">
    같은 검사를 진행하는 여러 장비가 서로 비슷한 결과를 내고 있는지 확인하기 위한 화면이에요.<br>
    기준 장비 1대와 최대 3대까지 한 번에 비교할 수 있어요.
  </p>
  <div class="two-col">
    <div class="field-box">
      <div class="field-title">비교 조건 (2가지)</div>
      <div style="font-size:12.5px; line-height:1.9; color:var(--gray); padding-top:4px;">
        <strong>A.</strong> [기준 장비]와 동일한 [결과일자 + 일련번호]로 매칭<br>
        = 정확히 '같은 조건에서 한 번에 비교'<br><br>
        <strong>B.</strong> [결과일자] 무시 후 결과일자로 정렬 후 매칭<br>
        = 정확히 같은 시점은 아니지만, 측정된 순서 기준으로 매칭
      </div>
    </div>
    <div>
      <h3 class="sub-title">계산 검증</h3>
      <p style="font-size:12.5px; color:var(--gray);">계산 검증 버튼을 누르면 통계 계산 검증창이 나오며, 검증을 화면에서 확인할 수 있어요.</p>
    </div>
  </div>
</div>
</section>

<!-- ─────────────────────────────────────────
     섹션: 환자 결과 확인
───────────────────────────────────────── -->
<section class="section" id="sec-patient">"""

if old_corr not in content:
    print("ERROR: correlation block not found"); exit(1)
content = content.replace(old_corr, new_corr)
print("3/5 correlation split OK")

# ── 4. Split sec-extended → sec-patient + sec-xbar ───────────
old_ext = """<section class="section" id="sec-patient">
<div class="page">
  <div class="chapter-header">
    <h1>Extended — 고급 기능</h1>
    <p>STEP 06 — 환자 데이터 조회 / X-Bar 차트 / X-Bar 마스터</p>
    <p class="intro-text">AgentQC 프로그램에서 정도관리 데이터만 확인하는 것이 아니라<br>
    <strong>환자 데이터도 가져와서 확인</strong>할 수 있도록 구현했어요. 그게 Extended 기능이에요!</p>
  </div>

  <h2 class="section-title">환자 결과 조회</h2>
  <div class="menu-path">메뉴 > AgentQC Extended > <span>환자 결과 조회</span></div>
  <table class="manual-table">
    <thead><tr><th>기능</th><th>설명</th></tr></thead>
    <tbody>
      <tr><td><strong>환자 데이터 조회</strong></td><td>단순한 환자 결과 조회 화면이에요.</td></tr>
      <tr><td><strong>데이터 검색</strong></td><td>검체번호로 데이터 검색</td></tr>
      <tr><td><strong>데이터 삭제</strong></td><td>좌측 리스트에서 우측 마우스 클릭 시, 삭제 화살표이 표시되고 선택 시 데이터 삭제됨</td></tr>
      <tr><td><strong>이미지 다운로드</strong></td><td>스캐터그램 이미지 우측 마우스 클릭 시, 이미지 다운로드 가능</td></tr>
    </tbody>
  </table>

  <h2 class="section-title" style="margin-top:22px;">X-Bar 차트 조회</h2>"""

new_ext = """<section class="section" id="sec-patient">
<div class="page">
  <div class="chapter-header">
    <h1>환자 결과 확인</h1>
    <p>STEP 02 — 환자 결과 조회</p>
    <p class="intro-text">AgentQC 프로그램에서 정도관리 데이터만 확인하는 것이 아니라<br>
    <strong>환자 데이터도 가져와서 확인</strong>할 수 있도록 구현했어요.</p>
  </div>

  <h2 class="section-title">환자 결과 조회</h2>
  <div class="menu-path">메뉴 > AgentQC Extended > <span>환자 결과 조회</span></div>
  <table class="manual-table">
    <thead><tr><th>기능</th><th>설명</th></tr></thead>
    <tbody>
      <tr><td><strong>환자 데이터 조회</strong></td><td>단순한 환자 결과 조회 화면이에요.</td></tr>
      <tr><td><strong>데이터 검색</strong></td><td>검체번호로 데이터 검색</td></tr>
      <tr><td><strong>데이터 삭제</strong></td><td>좌측 리스트에서 우측 마우스 클릭 시, 삭제 화살표이 표시되고 선택 시 데이터 삭제됨</td></tr>
      <tr><td><strong>이미지 다운로드</strong></td><td>스캐터그램 이미지 우측 마우스 클릭 시, 이미지 다운로드 가능</td></tr>
    </tbody>
  </table>
</div>
</section>

<!-- ─────────────────────────────────────────
     섹션: X-Bar
───────────────────────────────────────── -->
<section class="section" id="sec-xbar">
<div class="page">
  <div class="chapter-header">
    <h1>X-Bar</h1>
    <p>STEP 03 — X-Bar 차트 / X-Bar 설정</p>
    <p class="intro-text">환자 데이터를 일정한 갯수로 묶어 평균을 내고 변화를 관찰하는 <strong>X-Bar 차트</strong> 기능이에요.</p>
  </div>

  <h2 class="section-title">X-Bar 차트 조회</h2>"""

if old_ext not in content:
    print("ERROR: old_extended not found"); exit(1)
content = content.replace(old_ext, new_ext)
print("4/5 extended split OK")

# ── 5. Update STEP references in chapter-header <p> tags ─────
replacements = [
    # 홈 items
    ('<p>STEP 03 — 대시보드 화면 구성</p>', '<p>STEP 01 — 대시보드 화면 구성</p>'),
    ('<p>STEP 03 — 대시보드 기본 사용법</p>', '<p>STEP 01 — 대시보드 기본 사용법</p>'),
    ('<p>STEP 03 — QC 결과 확인</p>', '<p>STEP 01 — QC 결과 확인</p>'),
    ('<p>STEP 06 — 바코드를 생성하여 QC를 접수하거나 임시 검체를 접수</p>',
     '<p>STEP 01 — 바코드를 생성하여 QC를 접수하거나 임시 검체를 접수</p>'),
    ('<p>STEP 04 — QC 데이터 조회</p>', '<p>STEP 01 — QC 데이터 조회</p>'),
    ('<p>STEP 04 — Rule Refresh</p>', '<p>STEP 01 — Rule Refresh</p>'),
    # 정도관리 설정 STEP 02 → STEP 06
    ('<p>STEP 02 — 검사항목 마스터</p>', '<p>STEP 06 — 검사항목 마스터</p>'),
    ('<p>STEP 02 — QC LOT 마스터</p>', '<p>STEP 06 — QC LOT 마스터</p>'),
    ('<p>STEP 02 — LOT FAQ</p>', '<p>STEP 06 — LOT FAQ</p>'),
    ('<p>STEP 02 — 허용범위 설정 관리</p>', '<p>STEP 06 — 허용범위 설정 관리</p>'),
    ('<p>STEP 02 — 시약 마스터</p>', '<p>STEP 06 — 시약 마스터</p>'),
    ('<p>STEP 02 — 시약 LOT 마스터</p>', '<p>STEP 06 — 시약 LOT 마스터</p>'),
    # 프로그램 설정 STEP 02 → STEP 07
    ('<p>STEP 02 — 기본 마스터 관리</p>', '<p>STEP 07 — 기본 마스터 관리</p>'),
    ('<p>STEP 02 — 물질 마스터</p>', '<p>STEP 07 — 물질 마스터</p>'),
    ('<p>STEP 02 — 장비 마스터</p>', '<p>STEP 07 — 장비 마스터</p>'),
    # 로그인 STEP 01 → STEP 08
    ('<p>STEP 01 — 사용자 계정 만들기</p>', '<p>STEP 08 — 사용자 계정 만들기</p>'),
    ('<p>STEP 01 — 비밀번호 변경하기</p>', '<p>STEP 08 — 비밀번호 변경하기</p>'),
]
for old, new in replacements:
    content = content.replace(old, new)
print("5/5 STEP headers updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done — file saved.")
