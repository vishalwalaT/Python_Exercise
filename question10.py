n = int(input("Enter number of lines of triangle:"))
if n % 2 == 0:
    n += 1  # to make odd number to print triangle perfectly


def triangle(n):
    f = n // 2
    for i in range(0, n):
        for j in range(0, n):
            if (
                i == f
                or j == f
                or (((f - i) <= j <= (f + i)) and i <= f)
                or ((i > f) and (i - f) <= j <= (f * 2 - (i - f)))
            ):
                print(" ", end="")
            else:
                print("*", end="")
        print("")


# ****************************************
def triangle2(n):
    f = n // 2
    for i in range(0, n):
        for j in range(0, n):
            if (((f - i) <= j <= (f + i)) and i <= f) or (
                (i > f) and (i - f) <= j <= (f * 2 - (i - f))
            ):
                print("*", end="")
            else:
                print(" ", end="")
        print("")


triangle(n)
triangle2(n)

# ****************************************

for i in range(0, n):
    for j in range(0, n):
        if i == 0 or j == 0 or j == n - 1 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")


# ****************************************
k = 1
for i in range(0, n):
    for j in range(0, i + 1):
        print(k, end=" ")
        k += 1
    print("")

for i in range(0, n):
    for j in range(0, i + 1):
        if (i > 1 and i < n) and (j == 0 or j == i):
            print("*", end="")
        elif i <= 1 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
