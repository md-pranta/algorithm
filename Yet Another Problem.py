import sys


def input(): return sys.stdin.readline().strip()


N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
psum = [0] * (N + 1)
pointer = [float('-inf')] * (N + 1)
counter = [{0: 0}, {}]
zeros = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] ^ arr[i]

    if psum[i] in counter[(i + 1) % 2]:
        pointer[i] = counter[(i + 1) % 2][psum[i]]
    counter[i % 2][psum[i]] = i

    zeros[i] = zeros[i - 1]
    if arr[i] == 0:
        zeros[i] += 1

for _ in range(Q):
    l, r = map(int, input().split())

    if psum[r] ^ psum[l - 1]:
        print(-1)
        continue

    if zeros[r] - zeros[l - 1] == r - l + 1:
        print(0)
        continue

    if (r - l) % 2 == 0:
        print(1)
        continue

    if l > pointer[r]:
        print(-1)
        continue

    if arr[l] == 0 or arr[r] == 0:
        print(1)
        continue

    print(2)

