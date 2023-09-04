AP = [2, 5, 8, 11, 15, 17]
GP = [3, 9, 27, 81, 244, 729]
print("Wrong AP :", AP)
diff = AP[1] - AP[0]
for i in range(0, len(AP) - 1):
    if AP[i + 1] - AP[i] != diff:
        AP[i + 1] = AP[i] + diff
print("Corrected AP :", AP)
print("Wrong GP :", GP)
diff = GP[1] / GP[0]
for i in range(0, len(GP) - 1):
    if GP[i + 1] / GP[i] != diff:
        GP[i + 1] = int(diff * GP[i])
print("Corrected GP :", GP)
