a = int(input())
a_set = set(map(int, input().split()))

n = int(input())
for i in range(n):
    c = input().split()
    o_set = set(map(int, input().split()))
    if c[0] == 'intersection_update':
        a_set &= o_set
    elif c[0] == 'update':
        a_set |= o_set
    elif c[0] == 'symmetric_difference_update':
        a_set ^= o_set
    elif c[0] == 'difference_update':
        a_set -= o_set
        
total = 0
for x in a_set:
    total += x

print(total)