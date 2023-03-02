cube = lambda x: pow(x, 3)

def fibonacci(n):
    result = []
    for i in range(n):
        if i <= 1:
            result.append(i)
        else:
            result.append(result[i-1] + result[i-2])
    return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))