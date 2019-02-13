from sklearn.feature_extraction.text import CountVectorizer
data = []
data_labels = []
with open("./pos_tweets.txt") as f:
    for i in f: 
        data.append(i) 
        data_labels.append('pos')

with open("./neg_tweets.txt") as f:
    for i in f: 
        data.append(i)
        data_labels.append('neg')
vectorizer = CountVectorizer(
    analyzer = 'word',
    lowercase = False,
)
features = vectorizer.fit_transform(
    data
)
print("printing features")
print(features)


features_nd = features.toarray() # for easy usage
print("printing features_nd")
print(features_nd)
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test  = train_test_split(
        features_nd, 
        data_labels,
        train_size=0.80, 
        random_state=1234)
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)
y_pred = log_model.predict(X_test)
import random
j = random.randint(0,len(X_test)-7)
for i in range(j,j+7):
    print(y_pred[i])
    ind = features_nd.tolist().index(X_test[i].tolist())
    print(data[ind].strip())
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

#############
print('testing custom sentence now')
feat = vectorizer.transform(['"this is a really good sentence, i love it."'])
print(feat)
prediction = log_model.predict(feat)
print(prediction[0])
#############
from sklearn.externals import joblib
joblib.dump(log_model, '/data/mymodel.pkl')
joblib.dump(vectorizer, '/data/vect.pkl')
