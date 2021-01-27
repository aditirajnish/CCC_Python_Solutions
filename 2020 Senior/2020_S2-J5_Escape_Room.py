
# AC (15/15), stores cell numbers and cells it can travel to in dictionary

"""
sample input (outputs yes):
3
4
3 10 8 14
1 11 12 12
6 2 3 9
"""

def main():
    rows, cols = int(input()), int(input())

    end_value = rows * cols

    # key: number in cell
    # value: list of cell numbers to travel to
    cells = {}
    # cells = {3: [1, 9],
    #         10: [2],
    #          8: [3],
    #         14: [4],
    #          1: [2],
    #         11: [4],
    #         12: [6, 8],
    #          6: [3],
    #          2: [6],
    #          9: [16]}

    for r in range(1, rows + 1):
        row = list(map(int, input().split()))
        for c in range(1, cols + 1):
            key = row[c - 1]
            value = r * c
            if key in cells.keys():
                cells[key].append(value)
            else:
                cells[key] = [value]

    neighbours = [end_value] # cell numbers to be searched, starting with
                             # cell number pointing to last cell (backtracking)

    while neighbours: # loop runs while there are neighbours to be searched
        next_neighbours = [] # cell numbers to be searched after neighbours is searched

        for key in neighbours:
            if key == 1:
                return "yes"
            try:
                values = cells[key] # first cell is found
                next_neighbours.extend(values) # next neighbours to be searched
                cells.pop(key) # do not revisit key (infinite loop)
            except KeyError: # if key does not exist
                pass
        neighbours = next_neighbours # search next set of neighbours

    return "no" # when no more neighbours can be searched, loop ends

print(main())
