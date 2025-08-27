import sys
import math
import string


cases = int(sys.stdin.readline())
for caseNum in range(cases):
    inputt = input('')
    num1, num2 = inputt.split(' ')
    add = int(num1) + int(num2)
    multiply = int(num1) * int(num2)
    print(add,multiply)
    