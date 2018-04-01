import pandas as pd
import matplotlib.pyplot as plt

# Punkte
plt.figure(figsize=(12,12))
plt.scatter(g.date_diff.mean(),g.size(),edgecolor = 'none',alpha = 0.2, s=20, c='b')
plt.xlabel('Group mean relative date')
plt.ylabel('Group size')
plt.title('Train');

# einzelnes feature:
plt.hist(x, bins=100)
plt.plot(x, '.')

# zwei features:
plt.scatter(x, y)
pd.scatter_matrix(df) # alle features paarweise
df.corr()
plt.matshow()
# statistische Eigenschaften der features, z.B. für jedes feature den Mittelwert plotten, die features danach sortieren
# -> sehen, ob ein int. Bild rauskommt
df.mean().sort_values().plot(style='.')

plt.bar([1, 2, 3], [4, 5, 6])

df = pd.DataFrame({'A': [1, 2, 3], 'B': [7, 2, 8]})
plt.bar(df)

# einfacher plot
x = np.linspace(-1, 1, 100) # 100 linearly spaced numbers
y = x*x
plt.plot(x, y)

plt.show()
