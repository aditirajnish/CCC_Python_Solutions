
# 15/15 points

flips = input()

horizontal = flips.count("H")
vertical = len(flips) - horizontal

is_horizontal = horizontal % 2
is_vertical = vertical % 2

if is_horizontal and is_vertical:
    print("4 3\n2 1")

elif not is_horizontal and is_vertical:
    print("2 1\n4 3")

elif is_horizontal and not is_vertical:
    print("3 4\n1 2")

elif not is_horizontal and not is_vertical:
    print("1 2\n3 4")

else:
    print("Error")
