numbers = [2, 5, 6, 1, 3, 8, 9, 10]
lgth = len(numbers)
# bubble sort
for i in range(0, lgth):
    for j in range(i, lgth):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)
