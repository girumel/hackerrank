m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

for x in sorted(list(n_set ^ m_set)):
    print(x)
