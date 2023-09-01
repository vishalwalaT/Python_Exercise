string = "PQRQRQRQ"
substring = "QRQ"

count = 0
lgth = len(string)
lgth_substr = len(substring)
for i in range(0, lgth):
    if substring == string[i : i + lgth_substr]:
        count += 1
print(count)
