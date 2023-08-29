import collections

names = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
]

name_len = []

for i in names:
    name_len.append(len(i))

name_counter = collections.Counter(name_len)

list_key = sorted(list(name_counter.keys()))


def most():
    for k in list_key[0:3]:
        v = name_counter[k]
        lest = []
        for i in names:
            if k == len(i):
                lest.append(i)
        print("{} Name of length {}".format(v, k), lest)


def least():
    for k in list_key[-1:-4:-1]:
        v = name_counter[k]
        lest = []
        for i in names:
            if k == len(i):
                lest.append(i)
        print("{} Name of length {}".format(v, k), lest)


print("--------------Most Frequents Names----------------", end="\n \n")
most()
print("--------------Least Frequents Names----------------", end="\n \n")
least()
