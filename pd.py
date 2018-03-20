import pandas as pd
import numpy as np

# groupBy-Operationen (geht bestimmt noch eleganter)
df = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [7, 2, 0, 8], 'C': [1, 2, 3, 4], 'D': ['This', 'is', 'a', 'string']})
grouped = df.groupby('A')
t = pd.DataFrame()
for group, gdf in grouped:
    a = gdf.A.iloc[0]
    b = sum(gdf.B)
    c = sum(gdf.C)
    d = gdf.loc[gdf.B == max(gdf.B)].iloc[0]['D']
    t = t.append(pd.DataFrame({'A': [a], 'B': [b], 'C': [c], 'D': [d]}))

print(t)

# column und index (default: 0, 1,...)
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'], index=[10, 11])
df.drop(10, inplace=True)  # löscht die row mit index 10 (inplace=True ändert df selbst)
a = df.reset_index(drop=True)  # berechnet den Index neu, schmeißt den alten weg
assert a.first_valid_index() == 0


# loc gibt eine Zeile oder ein Element im df an (ranges gehen auch):
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
df.loc[23] = [5, 6]
assert df.loc[23, 'A'] == 5

# Werte in column 'A'
assert np.array_equal(df.A.unique(), np.array([1, 3, 5]))

# zwei dfs zu einem mergen (how='left|right|outer|inner'):
left = pd.DataFrame([[1, 'a1'], [2, 'a2'], [3, 'a3']], columns=['key', 'A'])
right = pd.DataFrame([[1, 'b1'], [2, 'b2']], columns=['key', 'B'])
merged = pd.merge(left, right, on='key', how='left')
assert(len(merged) == 3)

# rows mit fehlenden Werten
with_nan = merged[pd.isnull(merged).any(axis=1)]
# rows mit fehlenden Werten in bestimmter Spalte
with_nan = merged[merged['B'].isnull()]

print(type(merged.columns))
print(type(merged.columns.values))
for col in merged.columns:
    print(col)

# Werte durch andere ersetzen
df['label'] = df.label.map({'ham':0, 'spam':1})

# nach Werten filtern
rejected_df = train_df.loc[train_df['project_is_approved'] == 0]

# Statistik
train_df['project_essay_1_len'].describe()

# Ausrufezeichen zählen
df = pd.DataFrame([['a1!!', 'b1'], ['a2!', 'b2'], ['a3', 'b3']], columns=['A', 'B'])
df['count'] = df.A.map(lambda s: s.count('!'))
print(df)

s = 'abca'
s.count('a')

# apply vs map: map geht nur mit Series, apply auch mit DataFrame. Weitere Unterschiede noch unklar.
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df.head())
applied = df.A.apply(lambda x: x+1)
print(applied.head())
mapped = df.A.map(lambda x: x+1)
print(mapped.head())

# Series mit gleichem Index als Spalte zu df hinzufügen
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
series = pd.Series([7, 8, 9])
df['C'] = series.values

# Varianz: ddof (delta degrees of freedom) ist standardmäßig 1 (unbiased variance). In der WS (im Ggs. zur Statistik)
# ist ddof=0 normal (biased variance).
s = pd.Series([-1, 0, 1])
v = s.var(ddof=0)

# query mit Parameter:
tx_dec14_shop25 = transactions.query('shop_id == @shop_id & year == 14 & month == 12')

# nans auffüllen:
df = pd.DataFrame({'A': [1, 2], 'B': [3, np.nan]})
df.fillna(0, inplace=True)

# columns löschen:
df.drop(['B', 'C'], axis=1, inplace=True)

# nützliche Funktionen, um vorhandene Datentypen und Werte zu sehen:
df.dtypes
df.info()
df.describe()
df.A.nunique(dropna=False)  # number of unique values (geht auch für ganzen df), einschließlich nan
df.A.value_counts() # Vorkommen der einzelnen Werte (nur für series)
df.isnull()  # liefert einen dataframe von gleichem shape wie das Original, aber mit booleans
df.isnull().sum()  # liefert eine series mit den Spaltennamen als Index, True wird als 1 interpretiert

# df auf Festplatte speichern
import pickle
pickle.dump(df, open('dumped.p', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
loaded = pickle.load(open("dumped.p", "rb"))
