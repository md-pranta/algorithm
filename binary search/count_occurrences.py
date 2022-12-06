def count(nums, target, n):
    leftIdx = binarySearch(nums, target, True)
    rightIdx = binarySearch(nums, target, False) - 1
    if leftIdx <= rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
        return [leftIdx, rightIdx]
    return [-1, -1]
    # i = first(arr, 0, n - 1, x, n)
    # if i == -1:
    # return i
    # j = last(arr, i, n - 1, x, n)

    # return j - i + 1;


def binarySearch(nums, target, lower):
    left, right, ans = 0, len(nums) - 1, len(nums)
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] > target or (lower and nums[mid] >= target):
            right, ans = mid - 1, mid
        else:
            left = mid + 1
    return ans


def first(arr, low, high, x, n):
    if high >= low:
        mid = (low + high) // 2

        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid - 1), x, n)
    return -1


def last(arr, low, high, x, n):
    if high >= low:

        # low + (high - low)/2
        mid = (low + high) // 2;

        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)
    return -1


arr = [8, 8, 8, 8, 8, 8]
x = 8
n = len(arr)
c = print(count(arr, x, n))
# print("%d occurs %d times " % (x, c))
