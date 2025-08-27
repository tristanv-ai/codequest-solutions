import sys

answers = []
cases = int(sys.stdin.readline())
for caseNum in range(cases):
    code = input('')
    brack1 = code.index('[')
    sp = brack1 + 1
    brack2 = code.index(']')
    num = code[sp:brack2]
    xc, yc = num.split(',')
    xc, yc = int(xc) -1, int(yc) -1
    n, w1, n, w2, n = code.split('"')
    w1 = list(w1.split(' '))
    w2 = list(w2.split(' '))
    w1, w2 = w1[xc], w2[yc]
    
    l = lambda w1, w2: answers.append('Verified') if {l1 for l1 in w1} == {l2 for l2 in w2} else answers.append('Intercepted')
    l(w1,w2)
for i in answers:
    print(i)
