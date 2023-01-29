if __name__ == '__main__':
    s = input()
    tests = []
    tests.append([i for i in s if i.isalnum()])
    tests.append([i for i in s if i.isalpha()])
    tests.append([i for i in s if i.isdigit()])
    tests.append([i for i in s if i.islower()])
    tests.append([i for i in s if i.isupper()])
    for i in tests:
        if len(i) != 0:
            print('True')
        else:
            print('False')