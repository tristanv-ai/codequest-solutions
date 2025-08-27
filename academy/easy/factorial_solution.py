import sys
def factorial(n):
    if n == 0 or n == 1:
        answer.append(1)
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        answer.append(result)

answer = []
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    n = int(input(''))
    factorial(n)
for i in answer:
    print(i)