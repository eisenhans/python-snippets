import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


text = ['Da steh ich nun, ich armer Tor',
        'und bin so klug als wie zuvor.']  # list of text documents
vectorizer = CountVectorizer()

# 1. fit() baut das Vokabular
vectorizer.fit(text)
print(vectorizer.vocabulary_)

# 2. transform() macht einen Vektor (eine document term matrix) aus einem Text
# Alternative: fit_transform macht beides auf einmal
vector = vectorizer.transform(text)  # encode document

# sparse matrix als normalen df anzeigen:
pd.DataFrame(vector.toarray(), columns=vectorizer.get_feature_names())

vector2 = vectorizer.transform(['Ich bin hungrig.'])
pd.DataFrame(vector2.toarray(), columns=vectorizer.get_feature_names())


