def average(array):
    heights = set(array)
    total = 0
    for height in heights:
        total += height
    return total / len(heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)