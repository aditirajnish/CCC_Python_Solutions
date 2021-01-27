
# verify if 3 by 3 table of integers is an arithmetic square

row_1 = list(map(int, input().split()))
row_2 = list(map(int, input().split()))
row_3 = list(map(int, input().split()))

if row_1[2] - row_1[1] != row_1[1] - row_1[0]:
    print(f"Incorrect (row_1): {row_1}")
if row_2[2] - row_2[1] != row_2[1] - row_2[0]:
    print(f"Incorrect (row_2): {row_2}")
if row_3[2] - row_3[1] != row_3[1] - row_3[0]:
    print(f"Incorrect (row_3): {row_3}")

for col in range(3):
    if row_1[col] - row_2[col] != row_2[col] - row_3[col]:
        print(f"Incorrect (col {col + 1}): [{row_1[col]}, {row_2[col]}, {row_3[col]}]")



