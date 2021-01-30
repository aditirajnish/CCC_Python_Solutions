
# 9/15 points

from copy import deepcopy

class Path():
    def __init__(self, r):
        self.pho_visited = {r}
        self.r_visited = {r}
        self.r = r
        self.length = 0


def main():
    n, m = input().split()
    pho = input().split()
    nodes = {}

    for _ in range(int(n) - 1):
        a, b = input().split()
        if a in nodes.keys():
            nodes[a].append(b)
        else:
            nodes[a] = [b]
        if b in nodes.keys():
            nodes[b].append(a)
        else:
            nodes[b] = [a]

    trimmed = False
    pop_nodes = []
    while not trimmed:
        trimmed = True
        for node in nodes.keys():
            adjacent_nodes = nodes[node]
            if len(adjacent_nodes) == 1 and node not in pho:
                nodes[adjacent_nodes[0]].remove(node)
                pop_nodes.append(node)
                trimmed = False
        for node in pop_nodes:
            nodes.pop(node)
        pop_nodes = []

    current_paths = []
    for p in pho:
        path = Path(p)
        current_paths.append(path)

    while current_paths:
        next_paths = []
        for path in current_paths:
            adjacent_restaurants = nodes[path.r]
            for r in adjacent_restaurants:
                if r not in path.r_visited:
                    next_path = deepcopy(path)
                    next_path.length += 1
                    next_path.r = r
                    next_path.r_visited.add(r)

                    if r in pho and r not in path.pho_visited:  # new pho restaurant
                        next_path.pho_visited.add(r)
                        next_path.r_visited = {r}
                        if len(pho) == len(next_path.pho_visited):
                            return next_path.length

                    next_paths.append(next_path)
        current_paths = next_paths


print(main())


