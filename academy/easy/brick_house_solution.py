import sys
def func(small, large, length):
    max_large_bricks = min(length // 5, large)
    remaining_length = length - (max_large_bricks * 5)
    if remaining_length <= small:
        final.append('true')
    else:
        final.append('false') 
final = []
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    stuff = input('')
    small, large, length = stuff.split(' ')
    small, large, length = int(small), int(large), int(length)
    func(small, large, length)
for i in final:
    print(i)