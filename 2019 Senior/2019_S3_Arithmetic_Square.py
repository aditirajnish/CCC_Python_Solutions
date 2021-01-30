
# 7/15 points

def check_int(value):
    try:
        return int(value)
    except ValueError:
        return value


def duplicate_row(table):
    if table[0][0] != 'X' and table[0][1] != 'X' and table[0][2] != 'X':
        if table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X':
            if table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X':
                table[1] = table[0]
                table[2] = table[0]
    elif table[1][0] != 'X' and table[1][1] != 'X' and table[1][2] != 'X':
        if table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X':
            if table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X':
                table[0] = table[1]
                table[2] = table[1]
    elif table[2][0] != 'X' and table[2][1] != 'X' and table[2][2] != 'X':
        if table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X':
            if table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X':
                table[0] = table[2]
                table[1] = table[2]
    return table


def duplicate_col(table):
    if table[0][0] != 'X' and table[1][0] != 'X' and table[2][0] != 'X':
        if table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X':
            if table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X':
                table[0][1] = table[0][0]
                table[1][1] = table[1][0]
                table[2][1] = table[2][0]
                table[0][2] = table[0][0]
                table[1][2] = table[1][0]
                table[2][2] = table[2][0]
    elif table[0][1] != 'X' and table[1][1] != 'X' and table[2][1] != 'X':
        if table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X':
            if table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X':
                table[0][0] = table[0][1]
                table[1][0] = table[1][1]
                table[2][0] = table[2][1]
                table[0][2] = table[0][1]
                table[1][2] = table[1][1]
                table[2][2] = table[2][1]
    elif table[0][2] != 'X' and table[1][2] != 'X' and table[2][2] != 'X':
        if table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X':
            if table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X':
                table[0][0] = table[0][2]
                table[1][0] = table[1][2]
                table[2][0] = table[2][2]
                table[0][1] = table[0][2]
                table[1][1] = table[1][2]
                table[2][1] = table[2][2]
    return table


def solver(table):
    # solving for lone x in a row/col
    changeFlag = False

    # row[X] == table[i][X]
    for row in table:
        if row[0] == 'X' and row[1] != 'X' and row[2] != 'X':
            row[0] = row[1] - row[2] + row[1]
            changeFlag = True
        if row[1] == 'X' and row[0] != 'X' and row[2] != 'X':
            row[1] = (row[2] - row[0]) / 2 + row[0]
            changeFlag = True
        if row[2] == 'X' and row[0] != 'X' and row[1] != 'X':
            row[2] = row[1] - row[0] + row[1]
            changeFlag = True
        if row[0] != 'X' and row[1] != 'X' and row[2] != 'X':
            table = duplicate_row(table)

    # col[X] = table[X][i]
    for col in range(2):
        if table[0][col] == 'X' and table[1][col] != 'X' and table[2][col] != 'X':
            table[0][col] = table[1][col] - table[2][col] + table[1][col]
            changeFlag = True
        if table[1][col] == 'X' and table[0][col] != 'X' and table[2][col] != 'X':
            table[1][col] = (table[2][col] - table[0][col]) / 2 + table[0][col]
            changeFlag = True
        if table[2][col] == 'X' and table[0][col] != 'X' and table[1][col] != 'X':
            table[2][col] = table[1][col] - table[0][col] + table[1][col]
            changeFlag = True
        if table[0][col] != 'X' and table[1][col] != 'X' and table[2][col] != 'X':
            table = duplicate_col(table)

    # start filling in corners
    if not changeFlag:
        isEven = False
        if table[0][0] != 'X':
            isEven = table[0][0] % 2 == 0
        elif table[0][2] != 'X':
            isEven = table[0][2] % 2 == 0
        elif table[2][0] != 'X':
            isEven = table[2][0] % 2 == 0
        elif table[2][2] != 'X':
            isEven = table[2][2] % 2 == 0

        if table[0][0] == 'X':
            table[0][0] = 2 if isEven else 1
        elif table[0][2] == 'X':
            table[0][2] = 2 if isEven else 1
        elif table[2][0] == 'X':
            table[2][0] = 2 if isEven else 1
        elif table[2][2] == 'X':
            table[2][2] = 2 if isEven else 1

    x_count = 0
    for row in table:
        for e in row:
            if e == 'X':
                x_count += 1

    if x_count:
        return solver(table)
    for row in table:
        print(*list(map(int, row)))


table = []

# [0][0], [0][1], [0][2]
# [1][0], [1][1], [1][2]
# [2][0], [2][1], [2][2]

for i in range(3):
    row = list(map(check_int, input().split()))
    table.append(row)

solver(table)
