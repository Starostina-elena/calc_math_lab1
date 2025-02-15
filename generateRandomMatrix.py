from random import randint

n = 20

x_value = [randint(-5, 5) for i in range(n)]
matrix = []

for i in range(n):
    line = [randint(-5, 5) for j in range(n)]
    line[i] = max(line) * n + 1
    line.append(sum([x_value[j] * line[j] for j in range(n)]))
    matrix.append(line)

with open('input2.txt', mode='w') as f:
    f.write('0.01\n')
    f.write(f'{n}\n')
    for line in matrix:
        f.write(' '.join(map(str, line)) + '\n')

with open('answer2.txt', mode='w') as f:
    f.write(' '.join(map(str, x_value)) + '\n')
