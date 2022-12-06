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


n, q = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in b:
    print(search(a, i) + 1)