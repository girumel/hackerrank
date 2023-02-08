from collections import OrderedDict

n = int(input())
sales = OrderedDict()
for i in range(n):
    net_price = 0
    item = input().split()
    item_name = ' '.join(item[:-1])
    item_price = int(item[-1])
    if item_name in sales:
        net_price = sales[item_name]
        net_price += item_price
        sales[item_name] = net_price
    else:
        sales[item_name] = item_price
        
for item_name, item_price in sales.items():
    print(item_name, item_price)