import sys

def colorsort(color):
    if color == 'red':
        answers.append(f'No colors need to be mixed to make {color}.')
    elif color == 'red-violet':
        answers.append(f'In order to make {color}, blue and red must be mixed.')
    elif color == 'violet':
        answers.append(f'In order to make {color}, blue and red must be mixed.')
    elif color == 'blue-violet':
        answers.append(f'In order to make {color}, blue and red must be mixed.')
    elif color == 'blue':
        answers.append(f'No colors need to be mixed to make {color}.')
    elif color == 'blue-green':
        answers.append(f'In order to make {color}, blue and yellow must be mixed.')
    elif color == 'green':
         answers.append(f'In order to make {color}, blue and yellow must be mixed.')
    elif color == 'yellow-green':
        answers.append(f'In order to make {color}, blue and yellow must be mixed.')
    elif color == 'yellow':
        answers.append(f'No colors need to be mixed to make {color}.')
    elif color == 'yellow-orange':
        answers.append(f'In order to make {color}, red and yellow must be mixed.')
    elif color == 'orange':
        answers.append(f'In order to make {color}, red and yellow must be mixed.')
    elif color == 'red-orange':
        answers.append(f'In order to make {color}, red and yellow must be mixed.')
    

answers = []
cases = int(sys.stdin.readline())
for caseNum in range(cases):
    color = input('')
    colorsort(color)

for colors in answers:
    print(colors)