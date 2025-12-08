with open('day_three/input.txt') as f:
    batteries = [line for line in f.read().splitlines()]

total = 0
for battery in batteries:
    battery_jols = []
    for i in range(len(battery)):
        for j in range(i + 1, len(battery)):
            battery_jols.append(int(battery[i] + battery[j]))
    total += max(battery_jols)

print(total)


    
        
        