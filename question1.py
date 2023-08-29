import collections
l = [6, 55, 6, 3, 77, 35, 3, 2, 5, 63]

choice = 1
choice1 = "yes"
while choice != 6 and choice1 != "n":
    print("1. Length of list")
    print("2. Display first 3 number")
    print("3. Display sum of odd number")
    print("4. Number of duplicate number")
    print("5. Display list without duplicate numbers")
    print("6. Exit")
    choice = int(input("Enter Choice:"))
    print("")
    print("Original List :", l)
    print("")
    if choice == 1:
        print("Lenght of List :", len(l), end="\n")
    if choice == 2:
        print("First 3 elements :", l[0], l[1], l[2], end="\n")
    if choice == 3:
        sum = 0
        for x in l:
            if x % 2 != 0:
                sum = sum + x
        print("Sum of Odd Number:", sum, end="\n")

    if choice == 4:
        d = collections.Counter(l)
        count = 0
        for k,v in d.items():
            if v > 1 :
                count+=1
        print("Number of duplicate number :",count)
        
    if choice == 5:
        d = collections.Counter(l)
        new_list = []
        for k,v in d.items():
            if v == 1 :
                new_list.append(k)
        print("List without duplicate :", new_list, end="\n")

    if choice != 6:
        if input("Type 'y' for yes and 'n' for no : ") == 'n':
            break
