import sys
def slg(name,atbats):
    singles = 0
    doubles = 0
    triples = 0
    hrs = 0
    tab = 0
    for i in atbats:
        if i == 'BB':
            pass
        elif i == '1B':
            singles += 1
            tab += 1
        elif i == '2B':
            doubles += 1
            tab += 1
        elif i == '3B':
            triples += 1
            tab += 1
        elif i == 'HR':
            hrs += 1
            tab += 1
        elif i == 'K':
            tab += 1
    if tab == 0:
        answers.append(f'{name}=0.000')
    else:
        SLG = format(((1 * singles) + (2 * doubles) + (3 * triples) + (4 * hrs))/tab, '.3f')
        answers.append(f'{name}={SLG}')

answers = []

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    all = input('')
    name, atbats = all.split(':')
    atbats = atbats.split(',')
    slg(name,atbats)

for i in answers:
    print(i)