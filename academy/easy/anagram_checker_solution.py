import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    question = input('')
    word1, word2 = question.split('|')
    letters1 = {letter for letter in word1}
    letters2 = {let for let in word2}
    if word1 == word2:
        print(question,"= NOT AN ANAGRAM")
    elif letters1 == letters2:
        print(question,'= ANAGRAM')
    else:
        print(question,"= NOT AN ANAGRAM")

