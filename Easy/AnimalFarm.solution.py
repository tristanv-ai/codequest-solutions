import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    animals = input('')
    turkeys, goats, horses = animals.split(' ')
    turkey_legs = int(turkeys) * 2
    goat_legs = int(goats) * 4
    horse_legs = int(horses) * 4
    total_legs = turkey_legs + goat_legs + horse_legs
    print(total_legs) 
