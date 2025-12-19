with open('2025/two/input.txt') as f:
    ranges = [list(map(int, item.split('-'))) for item in f.read().split(',')] 
    numbers = sum((list(range(a, b + 1)) for a, b in ranges), [])

# remove the new line
#list_id[-1] = list_id[-1][:-2]
invalid_sum = 0

for num in numbers:
    s = str(num)
    for i in range(2, len(s) + 1):
        if len(s) % i == 0 and s[:len(s) // i] * i == s:
            invalid_sum += num
            break

print(ranges)