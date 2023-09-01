import collections

sentences = [
    "My name is Ram",
    "He is a good person",
    "You should be careful while coding",
    "He can do better",
    "The person is mysterious",
    "Jay Shree Ram",
    "It is my pen.",
]
l = []
dict_count = {}
for i in sentences:
    x = i.split(" ")
    l.extend(x)
print(collections.Counter(l))
