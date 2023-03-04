def reverseArray(a):
    r = []
    n = len(a) - 1
    while n >= 0:
        r.append(a[n])
        n -= 1
    return r

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(' '.join(map(str, reverseArray(a))))