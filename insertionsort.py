# recursive insertion sort

from random import randrange

def insertionsort(l):
    if len(l) < 2:
        return l
    h = l[0]
    res = insert(h, insertionsort(l[1:]))
    return res

def insert(e, l):
    if l == []:
        return [e]
    if e < l[0]:
        return [e] + l
    else:
        return [l[0]] + insert(e, l[1:])


# test
elem_range = 100
size = 10
l = [randrange(0,elem_range) for _ in range(size)]
print(l)
print(insertionsort(l))
