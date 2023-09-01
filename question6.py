string = "PQRQRQRQ"
substring = "QRQ"

count = 0
str_length = len(string)
substr_length = len(substring)
for i in range(0, str_length):
    if substring == string[i : i + substr_length]:
        count += 1
print(count)
