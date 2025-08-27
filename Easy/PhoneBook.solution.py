import sys
def formating(pn):
    if f == 'PARENTHESES':
        formatted = f"({pn[:3]}) {pn[3:6]}-{pn[6:]}"
        phonebook.append(formatted)
    elif f == 'DASHES':
        formatted = f"{pn[:3]}-{pn[3:6]}-{pn[6:]}"
        phonebook.append(formatted)
    elif f == 'PERIODS':
        formatted = f"{pn[:3]}.{pn[3:6]}.{pn[6:]}"
        phonebook.append(formatted)
        

phonebook = []
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    pf = input('')
    pn, f = pf.split(' ')
    formating(pn)
for i in phonebook:
    print(i)
