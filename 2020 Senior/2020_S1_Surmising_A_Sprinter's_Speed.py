
n = int(input())
times_and_positions = []

for _ in range(n):
    time, position = map(int, input().split())
    times_and_positions.append((time, position))

times_and_positions.sort()

max_speed = 0

for i in range(n - 1):
    time_1, position_1 = times_and_positions[i]
    time_2, position_2 = times_and_positions[i + 1]

    time = time_2 - time_1
    distance = abs(position_2 - position_1)

    speed = distance / time

    if speed > max_speed:
        max_speed = speed

print(max_speed)
