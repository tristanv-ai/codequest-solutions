import sys
def cs(n):
    nn = n
    l = 1
    while nn != 1:
        if nn % 2 == 0:
            nn = nn // 2
            l += 1
        elif nn % 2 != 0:
            nn = nn * 3 + 1
            l += 1
    answers.append(f'{n}:{l}')
answers = []
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    n = int(input(''))
    cs(n)
for i in answers:
    print(i)