# 섹션 구성 규칙

AgentQC 매뉴얼의 모든 기능 섹션은 아래 5개 블록을 순서대로 구성한다.

---

## 구조

```
[기능 개요]  →  [화면 구성]  →  [주요 기능]  →  [작업 순서]  →  [주의사항]
```

---

## 블록별 규칙

### 1. 기능 개요
- 태그: `<h2 class="section-title">기능 개요</h2>`
- 내용: 언제, 왜 이 화면을 여는지 1~3문장으로 설명
- 형식: `<p class="intro-text">...</p>`
- 다른 화면과 비교하거나, 이 기능만의 목적을 명확히 쓴다

### 2. 화면 구성
- 태그: `<h2 class="section-title">화면 구성</h2>`
- 영역은 **위 / 중앙 / 하단** 순서로 소제목 구분
- 소제목 형식: `<h3 class="sub-title">위 — 영역명</h3>`
- 조회 조건은 `field-box` 사용, 테이블 구성은 `manual-table` 사용
- 영역이 2개뿐이면 위 / 하단만 써도 됨

### 3. 주요 기능
- 태그: `<h2 class="section-title">주요 기능</h2>`
- 내용: 버튼, 메뉴, 액션 단위로 기술
- 형식: `manual-table` (기능 / 설명 2열)
- 조회 조건 필터 항목은 여기 쓰지 않는다 (화면 구성에서 처리)

### 4. 작업 순서
- 태그: `<h2 class="section-title">작업 순서</h2>`
- 내용: 실제 사용 흐름을 ① ② ③ … 순서로 기술
- 형식: `step-instruction` + `step-content` 반복
- 분기나 조건이 있으면 해당 step 안에 짧게 병기

### 5. 주의사항
- 태그: `<h2 class="section-title">주의사항</h2>`
- 내용: 사용자가 반드시 알아야 할 것, 실수하기 쉬운 것
- 형식: `notice-box` 사용. 여러 항목은 `notice-box`를 줄바꿈(`margin-top:10px`)으로 나열
- 주의사항이 없는 섹션은 이 블록을 생략한다

---

## HTML 패턴 요약

```html
<section class="section" id="sec-xxx">
<div class="page">
  <div class="page-contact">KAISER LAB 기술부 : 070-7770-0018(ARS 1번)</div>
  <div class="chapter-header">
    <h1>섹션 제목 (메뉴 경로)</h1>
  </div>

  <h2 class="section-title">기능 개요</h2>
  <p class="intro-text">...</p>

  <h2 class="section-title">화면 구성</h2>
  <h3 class="sub-title">위 — 영역명</h3>
  <!-- field-box 또는 manual-table -->
  <h3 class="sub-title">중앙 — 영역명</h3>
  <!-- manual-table -->
  <h3 class="sub-title">하단 — 영역명</h3>
  <!-- manual-table -->

  <h2 class="section-title">주요 기능</h2>
  <table class="manual-table">
    <thead><tr><th>기능</th><th>설명</th></tr></thead>
    <tbody>...</tbody>
  </table>

  <h2 class="section-title">작업 순서</h2>
  <div class="step-instruction">
    <div class="step-content"><strong>① ...</strong></div>
  </div>

  <h2 class="section-title">주의사항</h2>
  <div class="notice-box">...</div>
</div>
</section>
```
