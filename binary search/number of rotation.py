def minimum(arr, start, end, n):
    while start <= end:
        mid = start + (end - start) // 2
        prev = (mid - 1 + n) % n
        nex = (mid + 1) % n

        # Checking if mid is minimum
        if arr[mid] < arr[prev] \
                and arr[mid] <= arr[nex]:
            return mid
        elif arr[mid] >= arr[start]:
            return minimum(arr, start, mid - 1, n)


def countRotations(arr, n):
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        prev = (mid - 1 + n) % n
        nex = (mid + 1) % n

        # Checking if mid is minimum
        if arr[mid] < arr[prev] \
                and arr[mid] <= arr[nex]:
            return mid

        # if not selecting the unsorted part of array
        elif arr[mid] < arr[start]:
            return minimum(arr, start, mid - 1, n)
        elif arr[mid] > arr[end]:
            return minimum(arr, mid + 1, end, n)


# Driver code
def search(a, target):
    if not a:
        return -1
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == target:
            return mid
        if a[0] <= a[mid]:
            if a[0] <= target < a[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif a[mid] < target <= a[len(a) - 1]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr = [15, 18, 2, 3, 6, 12]
a = [12, 14, 16, 18, 2, 4, 6, 8]
N = len(a)
# print(countRotations(a, N))
print(search(a, 2))
