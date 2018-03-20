from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# CountVectorizer (bag of words)
cv = CountVectorizer(list_of_list_of_strings)
cv.fit()
cv.get_feature_names()  # Liste der Wörter
doc_array = cv.transform(documents)  # eine scipy sparse matrix
pd.DataFrame(data=doc_array.toarray(), columns=cv.get_feature_names())

# CountVectorizer mit naive Bayes
count_vector = CountVectorizer()
X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], df['label'], random_state=1)

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(X_train)
# Falls man sich die Matrix anschauen will, geht das so:
frequency_matrix = pd.DataFrame(data=training_data.toarray(), columns=count_vector.get_feature_names())
# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data = count_vector.transform(X_test)

naive_bayes = MultinomialNB()
naive_bayes.fit(X=training_data, y=y_train)
predictions = naive_bayes.predict(testing_data)

print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
print('Precision score: ', format(precision_score(y_test, predictions, pos_label='spam')))
print('Recall score: ', format(recall_score(y_test, predictions, pos_label='spam')))
print('F1 score: ', format(f1_score(y_test, predictions, pos_label='spam')))