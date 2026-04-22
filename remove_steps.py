"""
STEP 개념 제거:
1. nav-group-label 에서 'STEP XX ' 접두사 삭제
2. nav-item 내 <span class="nav-step">...</span> 삭제
3. chapter-header 내 <p>STEP XX — ...</p> 줄 삭제
4. CSS에서 .nav-step 관련 규칙 삭제
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. nav-group-label: "STEP XX " 접두사 제거
content = re.sub(
    r'(<div class="nav-group-label">)STEP \d+\s+',
    r'\1',
    content
)

# 2. nav-item 내 nav-step span 제거 (앞 공백 포함)
content = re.sub(
    r'\s*<span class="nav-step">.*?</span>\s*',
    ' ',
    content
)

# 3. chapter-header 내 STEP XX — ... 단락 제거
content = re.sub(
    r'\n[ \t]*<p>STEP \d+ — .*?</p>',
    '',
    content
)

# 4. CSS .nav-step 규칙 2개 제거
content = re.sub(
    r'\n\.nav-item \.nav-step \{[^}]+\}\n',
    '\n',
    content
)
content = re.sub(
    r'\n\.nav-item\.active \.nav-step \{[^}]+\}\n',
    '\n',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('완료')
