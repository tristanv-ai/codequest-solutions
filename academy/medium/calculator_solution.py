import sys
import math

def calculation(n1, s, n2):
    if s == '+':
        a1 = round((n1 + n2) + 1e-9, 1)
        answers.append(f"{a1} {a1}")
    elif s == '-':
        a1 = round((n1 - n2) + 1e-9, 1)
        a2 = round((n2 - n1) + 1e-9, 1)
        answers.append(f"{a1} {a2}")
    elif s == '*':
        a1 = round((n1 * n2) + 1e-9, 1)
        answers.append(f"{a1} {a1}")
    elif s == '/':
        a1 = round((n1 / n2) + 1e-9, 1)
        a2 = round((n2 / n1) + 1e-9, 1)
        answers.append(f"{a1} {a2}")

answers = []

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    math = input('')
    n1, s, n2 = math.split(' ')
    n1, n2 = float(n1), float(n2)
    calculation(n1, s, n2)

for i in answers:
    print(i)
    
