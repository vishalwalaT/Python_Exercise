Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]


def pairfind(n):
    lgth = len(Numbers)
    output = []
    for i in range(0, lgth):
        for j in range(i + 1, lgth):
            if (Numbers[i] + Numbers[j]) == n and (
                [Numbers[i], Numbers[j]] not in output
                and [Numbers[j], Numbers[i]] not in output
            ):
                output.append([Numbers[i], Numbers[j]])

    print(output)


pairfind(12)
