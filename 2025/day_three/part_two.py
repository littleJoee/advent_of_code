# part one was messy to i made another script
import functools

with open('day_three/input.txt') as f:
    batteries = [line for line in f.read().splitlines()]

total = 0

# magic script
@functools.cache
def func(val, digits):
    if digits == 0:
        return 0
    if len(val) == digits:
        return int(val)
    
    a = (int(val[0]) * 10 ** (digits - 1)) + func(val[1:], digits - 1)

    b = func(val[1:], digits)

    return max(a, b)

for battery in batteries:
    total += func(battery, 12)

print(total)