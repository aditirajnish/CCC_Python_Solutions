
number_of_games = int(input())

swift_runs = list(map(int, input().split()))
sema_runs = list(map(int, input().split()))

current_max_runs = 0
current_max_day = 0

swift_sum = 0
sema_sum = 0

for i in range(number_of_games):
    swift_sum += swift_runs[i]
    sema_sum += sema_runs[i]
    if swift_sum == sema_sum:
        if swift_sum > current_max_runs:
            current_max_runs = swift_sum
            current_max_day = i + 1

print(current_max_day)
