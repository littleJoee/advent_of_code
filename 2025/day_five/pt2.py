test_data = '''3-5
10-14
16-20
12-18'''

test = False
# parse the data: only te fresh id
if test:
    ids = [line for line in test_data.split('\n\n')]
else:
    with open('2025\day_five\input.txt') as f:
        ids = [line for line in f.read().split('\n\n')]

fresh = ids[0]
fresh_range = [list(map(int, id_range.split('-'))) for id_range in fresh.splitlines()]


# stack for deciding if to generate a range list
last = None
count = 0

for a, b in fresh_range:
    if last is None:
        last = (a, b)
    elif last[1] < a:
        count += last[1] - last[0] + 1
        last = (a, b)
    else:
        last = (last[0], max(last[1], b))

count += last[1] - last[0] + 1

print(count)