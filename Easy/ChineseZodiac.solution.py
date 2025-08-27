import sys
import math
def func():
    nn = number - 4
    an = nn % 10
    aa = math.floor(an / 2)
    tn = nn % 12
    final.append(f'{number}{ya}{elements[aa]}{animals[tn]}')

elements = ['Wood ','Fire ','Earth ','Metal ','Water ']
animals = ['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Goat','Monkey','Rooster','Dog','Pig']
final = []
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    number = int(input(''))
    if number % 2 == 0:
        ya = ' Yang '
        func()
    else:
        ya = ' Yin '
        func()
for i in final:
    print(i)