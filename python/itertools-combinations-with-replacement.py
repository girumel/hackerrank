from itertools import combinations_with_replacement

i = input().split()
s = sorted(i[0])
r = int(i[1])
for comb in list(combinations_with_replacement(s, r)):
    print(''.join(comb))