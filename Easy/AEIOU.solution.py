import sys
import math
import string

vowels = 0
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    sentences = input('')
    a = sentences.count('a')
    e = sentences.count('e')
    i = sentences.count('i')
    o = sentences.count('o')
    u = sentences.count('u')
    vowels = a + e + i + o + u
    print(vowels)      
