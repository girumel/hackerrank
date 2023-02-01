n = int(input())
s = set(map(int, input().split()))

c = int(input())
for i in range(c):
    c = input().split()
    if c[0] == 'pop':
        s.pop()
    elif c[0] == 'discard':
        s.discard(int(c[1]))
    elif c[0] == 'remove':
        s.remove(int(c[1]))

total = 0
for x in s:
    total += x
print(total)