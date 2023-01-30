def print_rangoli(size):
    width = 4 * size - 3
    sep = '-'
    abet_asc = [chr(i + 96) for i in range(1, size + 1)]
    abet_dsc = abet_asc[::-1] 
    i = 1
    j = len(abet_asc)
    while i < len(abet_dsc) + 1:
        rangoli = abet_dsc[:i] + abet_asc[j:]
        print(sep.join(rangoli).center(width, sep))
        i += 1
        j -= 1
    
    i = len(abet_asc) - 1
    j = 2
    while i > 0:
        rangoli = abet_dsc[:i] + abet_asc[j:]
        print(sep.join(rangoli).center(width, sep))
        i -= 1
        j += 1
            

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)