import re 

list_id = []

with open('two/input.txt') as f:
    list_id = f.read().split(',')

# remove the new line
list_id[-1] = list_id[-1][:-2]

def invalid_check(n):
    invalid_sum = 0

    for product_id in n:
        first, last = product_id.split('-')

        for i in range(int(first), int(last)):
            num = str(i)
            length = len(num)
 
            half = (length // 2)
            if num[:half] * 2 == num:
                invalid_sum += int(num)

    return invalid_sum

print(invalid_check(list_id))