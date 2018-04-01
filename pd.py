import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

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

# apply kann man mit dem Namen einer Methode verw., anstatt sie direkt aufzurufen - folgendes ist äquiv.:
X_tr.groupby('item_id').colname.apply('mean')
X_tr.groupby('item_id').colname.mean()

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
df.A.unique()  # ndarray
df.A.values  # ndarray
df.A.value_counts() # Vorkommen der einzelnen Werte (nur für series)
df.isnull()  # liefert einen dataframe von gleichem shape wie das Original, aber mit booleans
df.isnull().sum()  # liefert eine series mit den Spaltennamen als Index, True wird als 1 interpretiert

# df auf Festplatte speichern
import pickle
pickle.dump(df, open('dumped.p', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
loaded = pickle.load(open("dumped.p", "rb"))

#sortieren
df.sort_values('A')

# Datumswerte parsen
df = pd.DataFrame({'A': ['18.04.1969', '24.03.2018']})
df['parsed'] = pd.to_datetime(df.A)
df['weekday'] = df['parsed'].dt.weekday

# eine row löschen
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df.drop([1])  # nach index id
a2 = df.query('A == 2')
df.drop(df.A == 2)

# df und series mergen
df = pd.DataFrame([[1, 11], [1, 12], [2, 13]], columns=['shop_id', 'item_id'])
item_cnt = df.groupby(['shop_id', 'item_id'], as_index=False)['item_cnt'].sum()
pd.merge(df, df_item_cnt, how='left', on=['shop_id', 'item_id'])

# mehrere Dinge aus groupby aggregieren
minmax = df.groupby(['shop_id', 'item_id'], as_index=False).agg({'item_cnt': {'min_cnt': np.min, 'max_cnt': np.max}})
minmax.columns = ['shop_id', 'item_id', 'min_cnt', 'mac_cnt']

# diejenigen Werte einer Spalte, die als index einer series vork., durch die Werte der series ersetzen, alles andere
# durch nan
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
s = pd.Series([27, 76])
df.A.map(s)

# transform (bekommt Spalte gruppiert nach etwas als input und gibt series raus, die zum ungruppierten input passt)
df = pd.DataFrame({'A': [1, 1, 2], 'B': [3, 4, 5]})
df.groupby('A').transform('mean')
# im Gegensatz dazu gibt das hier (transform entfernt) eine Series, die zu der Gruppierung passt
df.groupby('A').mean()

# über rows iterieren (langsam):
for index, row in df.iterrows():
    print('index: {}, row: {}'.format(index, row))

# neue Spalte hinzufügen aus zwei vorhandenen:
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df['C'] = df['A'] + df['B']

# dasselbe mit Funktion:
df['C'] = df.apply(lambda row: row.A + row.B, axis=1)

# dasselbe schneller:
def f(df):
    return df.A + df.B

a = pd.Series([5, 11], index=[1, 2])
b = pd.Series([2, 3], index=[1, 2])

a = pd.DataFrame([5, 11], columns=['A'], index=[1, 2])
b = pd.DataFrame([2, 3], columns=['B'], index=[1, 2])
c = ((a['A'] - a.index) / b['B'])

# Spalten und Index:
df.columns
df.index

# just the indexing operator: [] - selektiert Spalten anhand des Labels (geht auch für rows, aber nicht empfohlen)
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
df['A']  # series
df[['A', 'C']]  # dataframe
df[['A']]  # dataframe
df.A  # Alternative dot notation

# loc[]
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=[1, 2, 3])
df.loc[1]  # gibt eine row als series aus (also gekippt)
df.loc[[1, 2]]  # Liste übergeben -> mehrere rows als df
df.loc[1:2]  # slicing - Besonderheit bei loc: das hintere Element ist dabei
df.loc[1, 'A']  # loc zum Selektieren von rows und cols - row_sel, col_sel
df.loc[:, 'A':'B']

# iloc[] ist wie loc[], aber selektiert nach index location
df.iloc[[0, 1], 1]  # hier ist bei slicing das hintere Element wieder nicht dabei

# boolean indexing/selection: Selektion durch Filtern der rows mit [] oder .loc[]
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# [] ist overloaded: normalerweise werden damit columns selektiert, wenn man eine sequence von booleans reingibt, rows.
df[[True, False]]  # Liste/Tupel/ndarray/series von booleans, Länge muss Anzahl der rows sein
s = pd.Series([1, 1], index=[0, 1])
df[df.A == s]  # Series: index muss gleich sein
df[df.A > 1]  # typische Verwendung: df.A > 1 liefert eine series von booleans
# boolesche Operatoren für pandas: &, |, ~
df[(df.A > 1) & ~(df.B < 4)]  # Um die Terme müssen Klammern.
# isin(): Methode von Series
df[df.A.isin([2, 3])]
# isnull() oder isna() (not applicable?): Methode von Series und DataFrame
df[df.A.isna()]
# series.between() - wird inklusiv verstanden
df[df.A.between(1, 1)]
# weil wir rows selektieren, geht das genauso mit loc. Aber da kann man nach dem Komma zusätzlich noch cols selektieren.
df.loc[df.A.between(1, 1)]
df.loc[df.A.between(1, 1), ['A']]
# Bem.: mit .iloc geht das im Prinzip auch, aber ist für Series nicht implementiert, d.h. man muss in Liste umwandeln.
# Aber auch nicht besser als loc, wird deshalb für boolean selection nicht verwendet.

# Werte zuweisen: generell müssen rechts vom = so viele Werte stehen, wie links selektiert wurden.
df['A'] = df['A'].astype(float)
df.loc[['Niko', 'Penelope', 'Aria'], 'FLOOR'] = [3, 6, 4]

# SettingWithCopyWarning: passiert dann, wenn man auf einer Kopie einen Wert setzen will. Manchmal ist die Kopie eine
# view, dann werden die Originaldaten geändert, manchmal eine copy, dann nicht. Ist ziemlich unintuitiv.
# Für Praxis einfach 2 Szenarien unterscheiden, dann bekommt man nie eine SettingWithCopyWarning:
# 1) Man will auf dem originalen df was setzen. Dann die selection nicht als chained selection machen, sondern in einem.
# 2) Man will auf einem abgeleiteten df was setzen, das Original soll unverändert bleiben. Dann df=df.copy() aufrufen.
df[df['age'] > 10]['score'] = 99  # falsch: hier wird 99 auf der copy gesetzt
df.loc[df['age'] > 10, 'score'] = 99  # richtig (Szenario 1)

# .at und .iat sind ähnlich wie .loc und .iloc, aber geben immer nur einen Skalar zurück. Etwas performanter. Besser
# nicht verwenden.

# reindex verwendet in der angegebenen axis diesen neuen Index. Vorhandene Spalten, die darin nicht vorkommen, werden
# gedroppt.
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df.reindex(['a', 'c'], axis=1, fill_value=0)

# Tabelle drehen - dasselbe macht df.transpose()
df.T

# Daten anhängen
df2 = pd.DataFrame({'a': [10, 11], 'b': [12, 13]})
df.append(df2, ignore_index=True)
pd.concat([df, df2], ignore_index=True)

s = pd.Series([1, 2, 3], index=[11, 12, 13])
s2 = pd.Series([5, 6, 7])