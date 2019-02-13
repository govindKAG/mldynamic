from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class Emote(object):
    def __init__(self):
        self.class_names = ["class:{}".format(str(i)) for i in range(2)]
        self.clf = joblib.load('/data/mymodel.pkl') 

    def predict(self,X,feature_names):
        vectorizer = joblib.load('/data/vect.pkl') 
        feat = vectorizer.transform(X[0])
        return np.asarray([[self.clf.predict(feat)[0]]])

    
