height = 11
print('')
print('\t\t\t   Merry Christmas <3\n')
for i in range(height):
    print('\t\t\t', end='')
    print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))
print('\t\t\t', end='')
print((' ' * height) + '|')
print()
