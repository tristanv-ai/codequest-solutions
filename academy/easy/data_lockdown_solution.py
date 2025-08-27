import sys

def checker(d):
    if d >= 1000:
        answers.append(f'{w} {d}')
    else:
        pass

answers = []

cases = int(sys.stdin.readline())
for caseNum in range(cases):
    logs = int(input(''))
    for i in range(logs):
        entry = input('')
        w, d = entry.split(' ')
        d = int(d)
        if '.lmco.com' in w:
            pass
        else:
            checker(d)

for i in answers:
    print(i)

