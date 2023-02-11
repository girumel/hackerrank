x = int(input())
sizes = list(map(int, input().split()))
n = int(input())
total = 0
for i in range(n):
    size, price = map(int, input().split())
    if size in sizes:
        total += price
        sizes.remove(size)
print(total)