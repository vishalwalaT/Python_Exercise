import functools


class Number:
    def __init__(self, number):
        self.number = number

    def get(self):
        return self.number

    def change_original_valuse(self, func: lambda x: x):
        new_number = list(map(func, self.number))
        return new_number

    def filter_values(self, func: lambda x: x):
        new_number = list(filter(func, self.number))
        return new_number

    def compound_the_number(self, func: lambda compound, x: compound + x):
        compound = functools.reduce(func, self.number)
        return compound

    def sort(self):
        new_number = sorted(self.number)
        return new_number


n1 = Number([2, 5, 1, 66, 22, 11, 10])

square = lambda x: x * 2
odd = lambda x: x % 2 != 0
reduc = lambda a, b: a + b
print("Number :", n1.get())
print("New Value :", n1.change_original_valuse(square))
print("Filtered Value :", n1.filter_values(odd))
print("Reduced Value :", n1.compound_the_number(reduc))
print("Sorted value :", n1.sort()) 
