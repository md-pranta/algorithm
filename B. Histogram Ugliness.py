import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


def solve(array, length):
    if length == 1:
        return array[0]
    cost = 0
    operation = 0
    for i in range(length):
        if i == 0:
            if array[i+1] < array[i]:
                operation += array[i] - array[i+1]
                cost += array[i+1]
            else:
                cost += array[i]
        elif i == n-1:
            if array[i] > array[i-1]:
                operation += array[i] - array[i-1]
                cost += array[i-1]
            else:
                cost += array[i]
        elif array[i] > array[i-1] and array[i] > array[i + 1]:
            if array[i-1] > array[i+1]:
                operation += array[i] - array[i-1]
                cost += array[i-1] - array[i+1]
            else:
                operation += array[i] - array[i+1]
                cost += array[i+1] - array[i-1]
        else:
            if array[i+1] < array[i]:
                cost += array[i] - array[i+1]
            elif array[i-1] < array[i]:
                cost += array[i] - array[i - 1]
    return cost+operation


for _ in range(N()):
    n = N()
    a = L()
    print(solve(a,n))