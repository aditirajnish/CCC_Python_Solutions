
# 15/15 points

option = input()
n = int(input())

d = sorted(list(map(int, input().split())))
p = sorted(list(map(int, input().split())))

total = 0

if option == '1':
    for i in range(n):
        total += max(d[i], p[i])

else:
    for i in range(n):
        total += max(d[i], p[n - i - 1])

print(total)
