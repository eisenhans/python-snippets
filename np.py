import numpy as np

# arrays erzeugen
np.zeros((m, n))
np.ones((m, n))
np.empty((m, n))  # beliebige Werte
np.array(list_or_tuple)  # dabei sind die Elemente von list/tuple Zahlen oder wieder list/tuple
np.arange(start, end, stepsize)  # ints von... bis
np.linspace(start, end, num_elements)  # floats von... bis

a = np.array([[1, 2, 3], [4, 5, 6]])

# über Zellen iterieren:
for (x,y), value in np.ndenumerate(a):
    print('x={}, y={}, value={}'.format(x, y, value))

# über rows iterieren:
for row in a:
    print(row)

# keine scientific notation verwenden:
np.set_printoptions(suppress=True)

# Eigenschaften aller/mancher Elemente prüfen:
if any(x > 5 for x in a):
    pass
