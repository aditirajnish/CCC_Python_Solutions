
# 15/15 points

first_string = input()
second_string = input()

first_string_table = []
asterisk_count = 0

for i in range(ord('a'), ord('z') + 1):
    s = chr(i)
    first_string_table.append(first_string.count(s))

for s in second_string:
    if s == '*':
        asterisk_count += 1
    else:
        i = ord(s) - ord('a')
        first_string_table[i] = first_string_table[i] - 1

for i in range(26):
    while asterisk_count > 0:
        if first_string_table[i] > 0:
            first_string_table[i] = first_string_table[i] - 1
            asterisk_count -= 1
        else:
            break

isAnagram = True

for i, e in enumerate(first_string_table):
    if e != 0:
        isAnagram = False

print("A" if isAnagram else "N")



