# https://en.wikipedia.org/wiki/Counting_sort

from random import randrange

def countingsort(l):
    occurs = [0] * (max(l)+1)
    out = []
    for e in l:
        occurs[e] += 1
    for i,e in enumerate(occurs):
        out += [i] * e
    return out


# test
elem_range = 100
size = 10
l = [randrange(0,elem_range) for _ in range(size)]
print(l)
print(countingsort(l))
