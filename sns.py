import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pt

df = pd.DataFrame(['A', 'A', 'A', 'B', 'B', 'C'], columns=['letters'])
data = df.letters.value_counts()
plot = sns.barplot(x=data.index, y=data)

# Balkendiagramm: Mittelwert nach Kategorie (mit Standardabweichung oder sowas)
sns.barplot(data=train_df, x='teacher_prefix', y="project_is_approved", hue=None)

# Verteilung der (nicht) approveden in Abhängigkeit vom Preis
facet = sns.FacetGrid(train_df, aspect=3, row=None, col=None, hue='project_is_approved')
facet.map(sns.kdeplot, 'total_price', shade=True)
facet.set(xlim=(0, train_df['total_price'].max()))
facet.add_legend()

# Heatmap
colormap = plt.cm.RdBu
plt.figure(figsize=(30, 30))
plt.title('Pearson Correlation of Features', y=1.05, size=25)
sns.heatmap(train_df.astype(float).corr(),linewidths=0.1,vmax=2.0,
            square=True, cmap=colormap, linecolor='white', annot=True, fmt='.2f')


# pt.show()


