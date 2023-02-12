import datetime

mm, dd, yyyy = map(int, input().split())
date = datetime.datetime(yyyy, mm, dd)
print((date.strftime('%A')).upper())