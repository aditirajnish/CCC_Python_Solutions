
# 15/15 points

number_of_villages = int(input())

villages = []
for i in range(number_of_villages):
    villages.append(int(input()))

villages.sort()

sizes = []

for i in range(1, number_of_villages - 1):
    current_village = villages[i]
    previous_village = villages[i - 1]
    next_village = villages[i + 1]

    left_size = (current_village - previous_village) / 2
    right_size = (next_village - current_village) / 2

    size = left_size + right_size
    sizes.append(size)

print(min(sizes))

