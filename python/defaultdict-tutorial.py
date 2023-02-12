n, m = map(int, input().split())
a, b = [input() for _ in range(n)], [input() for _ in range(m)]
for i in range(m):
    if b[i] in a:
        print(' '.join([str(j+1) for j in range(n) if a[j] == b[i]]))
    else:
        print(-1)