"""
menu-path div의 텍스트를 chapter-header h1 옆 괄호로 이동하고 div 삭제.
regex 기반으로 원본 HTML 형식을 최대한 보존.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def strip_tags(html):
    """HTML 태그 제거, 텍스트만 반환."""
    return re.sub(r'<[^>]+>', '', html).strip()

# section 단위로 분리하여 처리
section_re = re.compile(
    r'(<section\b[^>]*>)(.*?)(</section>)',
    re.DOTALL
)

# menu-path div (앞 공백줄 포함)
menu_path_re = re.compile(
    r'\n[ \t]*<div class="menu-path">(.*?)</div>',
    re.DOTALL
)

# chapter-header 내 h1
h1_in_header_re = re.compile(
    r'(<div class="chapter-header">.*?<h1>)(.*?)(</h1>)',
    re.DOTALL
)

def process_section(m):
    open_tag, body, close_tag = m.group(1), m.group(2), m.group(3)

    mp_matches = menu_path_re.findall(body)
    if not mp_matches:
        return m.group(0)

    # 각 menu-path의 텍스트 추출
    texts = [strip_tags(mp) for mp in mp_matches]
    combined = ' / '.join(texts)

    # h1 텍스트 뒤에 괄호 추가
    def replace_h1(hm):
        return hm.group(1) + hm.group(2).strip() + f' ({combined})' + hm.group(3)

    new_body = h1_in_header_re.sub(replace_h1, body, count=1)

    # menu-path div 제거 (앞 공백줄 포함)
    new_body = menu_path_re.sub('', new_body)

    return open_tag + new_body + close_tag

result = section_re.sub(process_section, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(result)

print('완료')
