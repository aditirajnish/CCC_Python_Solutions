
# 15/15 points

from sys import stdin

n = int(stdin.readline())

flowers = [list(map(int, stdin.readline().split())) for _ in range(n)]

# for the nth flower, as time passes, measurements increase
# rows are ordered, shortest to tallest flower
# if a flower is smaller than another, it is smaller for all measurements


def check_one(flowers_arrangement):
    for i in range(n):
        for j in range(n):
            current_flower = flowers_arrangement[i][j]
            try:
                right_flower = flowers_arrangement[i + 1][j]
                down_flower = flowers_arrangement[i][j + 1]
                if current_flower > right_flower or current_flower > down_flower:
                    return False
            except IndexError:
                pass
    return True

def display(array):
    for row in array:
        print(*row)

def check_all(flowers):
    if check_one(flowers):
        return flowers
    else:
        for _ in range(3):
            new_flowers = [[0 for a in range(n)] for b in range(n)]
            for i in range(n):
                for j in range(n):
                    f = flowers[i][j]
                    new_flowers[n - j - 1][i] = f
            flowers = new_flowers
            if check_one(flowers):
                return flowers


display(check_all(flowers))