# Python3 program to print count of values such
# that n+i = n^i

# function to count number of values less than
# equal to n that satisfy the given condition
def countValues(n):
    # unset_bits keeps track of count of un-set
    # bits in binary representation of n
    unset_bits = 0

    while (n):
        if n & 1 == 0:
            unset_bits += 1
        n = n >> 1

    # Return 2 ^ unset_bits
    x = 1 << unset_bits
    return x


# Driver code
if __name__ == '__main__':
    n = 18
    print(countValues(n))

# This code is contributed by rutvik
