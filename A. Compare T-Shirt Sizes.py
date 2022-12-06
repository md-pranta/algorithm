for _ in range(int(input())):
    a, b = input().split(' ')
    if a == b:
        print('=')
    else:
        if a[-1] == b[-1]:
            if a[-1] == 'L':
                if len(a) > len(b):
                    print('>')
                else:
                    print('<')
            else:
                if len(a) > len(b):
                    print('<')
                else:
                    print('>')
        elif ord(a[-1]) < ord(b[-1]):
            print('>')
        elif ord(a[-1]) > ord(b[-1]):
            print('<')