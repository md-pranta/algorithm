def solve(x, y, len_of_x, len_of_y):
    li = set()
    for i in range(len_of_x):
        for j in range(i, len_of_x):
            li.add(x[i:j + 1])

    length = 0
    for sub_string in li:
        if sub_string in y:
            length = max(len(sub_string), length)
    return len_of_x + len_of_y - 2 * length


for _ in range(int(input())):
    a = input()
    b = input()
    if len(a) > len(b):
        a, b = b, a
    print(solve(a, b, len(a), len(b)))
