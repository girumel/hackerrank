t = int(input())
for n in range(t):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))
    print('True' if set_a.issubset(set_b) else 'False')