mat_size = tuple(input().split())
N, M = mat_size
N, M = int(N), int(M)

i = (N // 2) * 3
j = 1
while (i >= 3):
    while (j <= N -2):
        print('-' * i + '.|.' * j + '-' * i)
        i -= 3
        j += 2    
print('WELCOME'.center(M, '-'))
i = 3
j = N - 2
while (i <= N + 2):
    while (j >= 1):
        print('-' * i + '.|.' * j + '-' * i)
        i += 3
        j -= 2