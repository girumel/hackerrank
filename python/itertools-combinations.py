from itertools import combinations

i = input().split()
s = sorted(i[0])
k = int(i[1])
n = 1
while n <= k:
    for comb in list(combinations(s, n)):
        print(''.join(comb))
    n += 1