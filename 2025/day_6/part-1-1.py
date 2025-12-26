with open('2025/day_6/input.txt') as f:
    lines = [line for line in f.read().splitlines()]
    matrix = [list(map(int, line.split())) for line in lines[:-1]]
    operations = lines[-1].split()
    total = 0
    for i in range(len(matrix[0])):
        result = matrix[0][i]
        for j in range(1, len(matrix)):
            if operations[i] == '+':
                result += matrix[j][i]
            elif operations[i] == '*':
                result *= matrix[j][i]
        total += result

print(total)
