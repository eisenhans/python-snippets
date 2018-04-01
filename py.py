a = [0, 1, 2, 3, 4, 5, 6, 7]

# slicing: a[slice], wobei slice durch start:stop:step gegeben sein kann
assert a[1:6:2] == [1, 3, 5]

b = a[:2]
a[0] = -1
b

