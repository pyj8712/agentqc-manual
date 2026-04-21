import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Nav order (target order)
nav_order = [
    'sec-intro',
    'sec-qc-result',
    'sec-dashboard',
    'sec-dashboard-basic',
    'sec-barcode',
    'sec-data-query',
    'sec-rule-refresh',
    'sec-patient',
    'sec-xbar',
    'sec-xbar-settings',
    'sec-correlation',
    'sec-reports',
    'sec-test-item',
    'sec-qc-lot',
    'sec-lot-faq',
    'sec-allowable',
    'sec-reagent',
    'sec-reagent-lot',
    'sec-basic-master',
    'sec-material',
    'sec-equipment',
    'sec-user-create',
    'sec-password',
]

# Split into: before first section / sections / after last section
first_sec = content.index('\n<section class="section')
before = content[:first_sec]

after_start = content.rindex('</section>') + len('</section>')
after = content[after_start:]

sections_block = content[first_sec:after_start]

# Extract each section block
# Pattern: from \n<!-- comment --> (optional) + <section...id="sec-xxx"> to </section>
# We'll split by looking for each section start
section_pattern = re.compile(
    r'(\n<!-- [^\n]+ -->\n     [^\n]+\n[^\n]+ -->\n)?'  # optional comment block
    r'\n<section class="section[^"]*" id="(sec-[^"]+)">'
    r'.*?'
    r'</section>',
    re.DOTALL
)

sections = {}
for m in section_pattern.finditer(sections_block):
    sec_id = m.group(2)
    sections[sec_id] = m.group(0)

print(f'Found {len(sections)} sections: {list(sections.keys())}')

missing = [s for s in nav_order if s not in sections]
if missing:
    print(f'MISSING: {missing}')

# Build reordered sections block
reordered = ''
for sec_id in nav_order:
    if sec_id in sections:
        reordered += sections[sec_id]
    else:
        print(f'SKIP (not found): {sec_id}')

new_content = before + reordered + after

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done.')
