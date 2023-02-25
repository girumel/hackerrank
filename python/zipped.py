n, x = map(int, input().split())
sheet = []
for i in range(x):
    mark = list(map(float, input().split()))
    sheet.append(mark)
for i in range(n):
    print(sum(list(zip(*sheet))[i]) / x)