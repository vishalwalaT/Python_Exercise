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
        # number = 0
        # visited = []
        # for x in l:
        #     i = 0
        #     count = 0
        #     if x not in visited:
        #         for y in l:
        #             if x == y:
        #                 count += 1
        #         if count > 1:
        #             number += 1
        #         visited.append(x)
        new_list = []
        for x in l:
            if x not in new_list and l.count(x) > 1:
                new_list.append(x)
        print("Number of duplicate number :", len(new_list))
        # print("Number of duplicate number :", number, end="\n")
    if choice == 5:
        new_l = []
        for x in l:
            count = 0
            for y in l:
                if x == y:
                    count += 1
            if count == 1:
                new_l.append(x)
        print("List without duplicate :", new_l, end="\n")

    if choice != 6:
        choice1 = input("Type 'y' for yes and 'n' for no : ")
