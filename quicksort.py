from random import randrange

def quicksort(l):
    if len(l) < 2:
        return l
    pivot = l[0]
    l1 = [x for x in l[1:] if x < pivot]
    l2 = [x for x in l[1:] if x >= pivot]
    return quicksort(l1) + [pivot] + quicksort(l2)


# test
elem_range = 100
size = 10
l = [randrange(0,elem_range) for _ in range(size)]
print(l)
print(quicksort(l))
