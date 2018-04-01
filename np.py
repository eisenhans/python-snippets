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

# arrays aneinangerhängen
a = np.array([1, 2, 3])
b = np.array([4, 5])
np.concatenate((a, b))

# mehrdimensionales slicing (start:stop:step)
# Um alle zu bekommen, kann man ':' schreiben oder diese dim einfach weglassen)
# Anders als bei plain python bekommt man mit sclicing eine view, d.h. wenn man danach das Original ändert, ändert sich
# auch die view.
a = np.array([[1, 2, 3], [4, 5, 6]])
assert (a[:1, :] == np.array([[1, 2, 3]])).all()

# broadcasting: fehlende Länge wird hinzugefügt, damit Operationen zw. arrays von untersch. Gestalt gehen
a = np.array([[0, 1, 2], [3, 4, 5]])
b = np.array([0, 1, 2])
a + b

# Matrizenmultiplikation dank explizitem broadcasting:
a = np.array([[1,2], [3,4], [5,6]])
b = np.array([1, 2, 3])
a * b[:, np.newaxis]  # genausogut: np.multiply(a, b[:, np.newaxis])
b[:, np.newaxis] * a

# Skalarprodukt (dot product)
b.dot(a)

# unique
np.unique(a, return_counts=True)
