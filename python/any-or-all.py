n = int(input())
a = list(map(int, input().split()))
positive = [True if x > 0 else False for x in a]
palindromic  = [True if str(x) == ''.join(reversed(str(x))) else False for x in a]
print(all(positive) and any(palindromic))