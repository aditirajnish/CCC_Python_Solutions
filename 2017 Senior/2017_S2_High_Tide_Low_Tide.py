
from collections import deque

n = int(input())
mixed_tides = list(map(int, input().split()))
new_tides = deque()

if n == 1:
    print(*mixed_tides)

elif n % 2 == 0:
    loops = int(n / 2)

    for _ in range(loops):
        cur_max = max(mixed_tides)
        mixed_tides.remove(cur_max)
        new_tides.appendleft(cur_max)

        cur_min = min(mixed_tides)
        mixed_tides.remove(cur_min)
        new_tides.appendleft(cur_min)

else:
    loops = int(n / 2)

    for _ in range(loops):
        cur_min = min(mixed_tides)
        mixed_tides.remove(cur_min)
        new_tides.appendleft(cur_min)

        cur_max = max(mixed_tides)
        mixed_tides.remove(cur_max)
        new_tides.appendleft(cur_max)

    new_tides.appendleft(mixed_tides[0])

print(*new_tides)
