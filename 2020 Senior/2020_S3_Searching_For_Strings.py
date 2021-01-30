
# 7/15 points

from sys import stdin

def main(n, h):

    if len(n) > len(h):
        return 0

    else:
        n_table = []
        h_table = [0 for _ in range(26)]
        permutations = set()

        for i in range(ord('a'), ord('z') + 1):
            s = chr(i)
            n_table.append(n.count(s))

        for i in range(len(n)):
            char = h[i]
            h_table[ord(char) - ord('a')] = h_table[ord(char) - ord('a')] + 1

        for i in range(len(n), len(h)):
            if n_table == h_table:
                permutations.add(h[i - len(n): i])
            h_table[ord(h[i - len(n)]) - ord('a')] = h_table[ord(h[i - len(n)]) - ord('a')] - 1
            h_table[ord(h[i]) - ord('a')] = h_table[ord(h[i]) - ord('a')] + 1

        if n_table == h_table:
            permutations.add(h[len(h) - len(n): len(h)])

        return len(permutations)

n = stdin.readline().strip('\n')
h = stdin.readline().strip('\n')

print(main(n, h))