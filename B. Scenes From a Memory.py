import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n = N()
    s = S()

    for i in '14689':
        if i in s:
            print(1)
            print(i)
            break
    else:
        if '2' in s[1:]:
            print(2)
            ind = s[1:].index('2')+1
            print(s[ind-1:ind+1])
        elif s.count('3') > 1:
            print(2)
            print(33)
        elif '5' in s[1:]:
            print(2)
            ind = s[1:].index('5')+1
            print(s[ind-1:ind+1])
        elif s.count('7') > 1:
            print(2)
            print(77)
        else:
            print(2)
            print(f'{s[0]}7')