numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]


def sumofnum(l):
    if len(l) <= 2:
        return l[0] + l[1]
    else:
        i = 1
    return l[0] + sumofnum(l[i::])


print(sumofnum(numbers))


# 0 1 1 2 3 5 8 13 21
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
