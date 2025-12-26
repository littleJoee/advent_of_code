with open('2025/day_6/input.txt') as f:
    exp = [[num for num in line.split()] for line in f.read().split('\n')]

str_nums = exp[:len(exp) - 1]
nums = []

# converting all the stings in the list to numbers
for line in str_nums:
    nums.append(list(map(int, (num for num in line))))

# holds the operators: *, +
oper = exp[-1]
count = 0

for i in range(len(oper)):
    match oper[i]:
        case '+':
            count += nums[0][i] + nums[1][i] + nums[2][i] + nums[3][i]
        case '*':
            count += nums[0][i] * nums[1][i] * nums[2][i] * nums[3][i]

print(count)