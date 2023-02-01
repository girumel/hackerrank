set_a = set(map(int, input().split()))
n = int(input())

for i in range(n):
    set_o = set(map(int, input().split()))
    if not set_a.issuperset(set_o):
        print('False')
        break
else:
    print('True')