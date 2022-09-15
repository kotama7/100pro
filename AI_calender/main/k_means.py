from numpy import random
from sklearn.cluster import KMeans
import pandas as pd
from .models import Schedule
from sklearn.model_selection import train_test_split
import pickle

def cleansing():
    pass

def clasifyer():
    pass

if __name__ == '__main__':
    dataset_obj = Schedule.objects.all()
    dataset = pd.DataFrame()
    clf = KMeans(n_clusters=3,random_state=0)
    x, y = cleansing()  #
    x_train, x_test, y_train , y_test = train_test_split(x,y)
    clf.fit(x_train,y_train)
    pickle.dump(clf,open('schedule.sav','wb'))
    print(f'the score of model is {clf.score(x_test,y_test)}')
