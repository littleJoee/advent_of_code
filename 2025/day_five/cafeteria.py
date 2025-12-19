test_data = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

test = False

# parse the data: separating using the blank line
if test:
    ids = [line for line in test_data.split('\n\n')]
else:
    with open('2025\day_five\input.txt') as f:
        ids = [line for line in f.read().split('\n\n')]

fresh, avail = ids
fresh_range = fresh.splitlines()
available_id = avail.splitlines()

# now we make the avai

total = 0
for num in available_id:
    for id_range in fresh_range:
        a, b = id_range.split('-')
        if int(a) < int(num) and int(num) < int(b):
            total += 1
            break
print(total)