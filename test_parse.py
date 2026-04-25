import re

def parse_test(filepath):
    content = None
    for enc in ('utf-8', 'utf-8-sig', 'cp1252', 'latin-1'):
        try:
            with open(filepath, 'r', encoding=enc) as f:
                content = f.read()
            print('Encoding OK:', enc)
            break
        except Exception:
            continue
    if not content:
        print('Cannot read file')
        return
    print('First 50 chars:', repr(content[:50]))
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        print('YAML FOUND')
        for line in match.group(1).split('\n')[:8]:
            print(' ', repr(line))
    else:
        print('NO YAML MATCH')

parse_test('08_DADOS_E_JOURNAL/JOURNAL_TRADES/PAPER_TRADE_003.md')
