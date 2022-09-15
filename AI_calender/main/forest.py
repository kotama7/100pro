from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

def cleansing(data:pd.DataFrame):
    x_data = data['x_data']
    y = data['y_data']
    x = pd.DataFrame()
    for i in range(len(y)):
        y[i] = int(y[i])
        x[i] = [ord(ele.ljust(100)[i]) for ele in x_data]
    return x,y

def classifyer(detail):
    clf = pickle.load(open('class.sav','rb'))
    


if __name__ == '__main__':
    clf = RandomForestClassifier()
    data = pd.read_csv('./dataset_detail.csv')
    x,y = cleansing(data)
    x_train ,x_test, y_train ,y_test = train_test_split(x,y,random_state=0)
    clf.fit(x_train,y_train)
    pickle.dump(clf,open('class.sav','wb'))
    print(f'the score is {clf.score(x_test,y_test)}')
