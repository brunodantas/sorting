# fully recursive mergesort

from random import randrange

def merge(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])

def mergesort(l):
    if len(l) < 2:
        return l
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    return merge(mergesort(l1), mergesort(l2))


# test
elem_range = 100
size = 10
l = [randrange(0,elem_range) for _ in range(size)]
print(l)
print(mergesort(l))
