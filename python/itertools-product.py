from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
products = list(product(a, b))
for product in products:
    print(product, end=' ')