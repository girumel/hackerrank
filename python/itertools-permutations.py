from itertools import permutations

i = input().split()
s = sorted(i[0])
r = int(i[1])
perms = list(permutations(s, r))
for perm in perms:
    print(''.join(perm))