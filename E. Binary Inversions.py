def solution(arr):
    ans = 0
    one = 0
    for i in arr:
        if i == 0:
            ans += one
        else:
            one += 1
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sol = solution(a)
    left0 = -1
    right1 = -1
    if 0 in a:
        left0 = a.index(0)
    if 1 in a:
        for k in range(n - 1, -1, -1):
            if a[k] == 1:
                right1 = k
                break
    b = a[:]
    if left0 != -1:
        a[left0] = 1
        sol = max(sol, solution(a))
        a[left0] = 0
    if right1 != -1:
        a[right1] = 0
        sol = max(sol, solution(a))
    print(sol)
