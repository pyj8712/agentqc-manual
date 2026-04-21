with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# (line_number 1-based, old_fragment, new_fragment)
fixes = [
    (459,  'STEP 01 —', 'STEP 08 —'),  # sec-user-create
    (568,  'STEP 01 —', 'STEP 08 —'),  # sec-password
    (631,  'STEP 02 —', 'STEP 07 —'),  # sec-basic-master
    (686,  'STEP 02 —', 'STEP 07 —'),  # sec-equipment
    (727,  'STEP 02 —', 'STEP 06 —'),  # sec-test-item
    (770,  'STEP 02 —', 'STEP 07 —'),  # sec-material
    (818,  'STEP 02 —', 'STEP 06 —'),  # sec-qc-lot
    (869,  'STEP 02 —', 'STEP 06 —'),  # sec-lot-faq
    (951,  'STEP 02 —', 'STEP 06 —'),  # sec-reagent
    (983,  'STEP 02 —', 'STEP 06 —'),  # sec-reagent-lot
    (1017, 'STEP 02 —', 'STEP 06 —'),  # sec-allowable
    (1083, 'STEP 03 —', 'STEP 01 —'),  # sec-dashboard
    (1133, 'STEP 03 —', 'STEP 01 —'),  # sec-dashboard-basic
    (1221, 'STEP 03 —', 'STEP 01 —'),  # sec-qc-result
    (1309, 'STEP 04 —', 'STEP 01 —'),  # sec-data-query
    (1365, 'STEP 04 —', 'STEP 01 —'),  # sec-rule-refresh
]

for lineno, old, new in fixes:
    idx = lineno - 1
    if old in lines[idx]:
        lines[idx] = lines[idx].replace(old, new)
        print(f'OK line {lineno}: {old} -> {new}')
    else:
        print(f'MISS line {lineno}: "{old}" not found in: {lines[idx].strip()}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done.')
