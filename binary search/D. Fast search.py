def search(array, key):
    begin = -1
    end = len(array)
    while begin + 1 < end:
        mid = (begin + end) >> 1
        if array[mid] >= key:
            end = mid
        else:
            begin = mid
    return end


def rsearch(array, key):
    begin = -1
    end = len(array)
    while begin + 1 < end:
        mid = (begin + end) >> 1
        if array[mid] <= key:
            begin = mid
        else:
            end = mid
    return begin


n = int(input())
a = sorted(map(int, input().split()))
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(rsearch(a, r) - search(a, l) + 1, end=' ')
print()
