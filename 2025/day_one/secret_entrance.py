def part_one():
    count = 0  # password

    current_number = 50
    dial_turns = []

    with open('2025/day_one/input.txt') as f:
        dial_turns = f.read().split('\n')

    for line in dial_turns:
        if not line[1:]:
            continue
        turn_dist = int(line[1:])

        if line[0] == 'L': 
            # subtract
            for i in range(turn_dist):
                current_number -= 1
                if current_number < 0:
                    current_number = 99
        else:
            # add
            for i in range(turn_dist):
                current_number += 1
                if current_number > 99:
                    current_number = 0

        if current_number == 0:
            count += 1
    return count

def part_two():
    
    count = 0  # password

    current_number = 50
    dial_turns = []

    with open('day_one/input.txt') as f:
        dial_turns = f.read().split('\n')

    for line in dial_turns:
        if not line[1:]:
            continue
        turn_dist = int(line[1:])

        if line[0] == 'L': 
            # subtract
            for i in range(turn_dist):
                current_number -= 1
                if current_number < 0:
                    current_number = 99
                if current_number == 0:
                    count += 1
        elif line[0] == 'R':
            # add
            for i in range(turn_dist):
                current_number += 1
                if current_number > 99:
                    current_number = 0
                if current_number == 0:
                    count += 1
    return count

print('Part one answer: ' + str(part_one()))
print('part two answer: ' + str(part_two()))
