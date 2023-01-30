def print_formatted(number):
    w = len('{0:b}'.format(number))
    for i in range(1, number + 1):
        decimal = '{0:d}'.format(i)
        octal = '{0:o}'.format(i)
        hexa = '{0:X}'.format(i)
        binary = '{0:b}'.format(i)
        print(decimal.rjust(w), octal.rjust(w), hexa.rjust(w), binary.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)