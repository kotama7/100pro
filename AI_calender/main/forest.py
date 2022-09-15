from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

def cleansing(data:pd.DataFrame):
    x_data = data['x_data']
    y_data = data['y_data']
    x = pd.DataFrame()
    y = pd.DataFrame([int(ele) for ele in y_data])
    for i in range(len(x_data)):
        x[i] = [ord(ele.ljust(100)[i]) for ele in x_data]
    print(x,y)
    return x,y

def classifyer(detail:str):
    clf = pickle.load(open('class.sav','rb'))
    x = pd.DataFrame([ord(ele) for ele in detail.ljust(100)])
    ans = clf.predict(x)
    return str(ans)


if __name__ == '__main__':
    clf = RandomForestClassifier(n_estimators=1)
    data = pd.read_csv('./dataset_detail.csv')
    x,y = cleansing(data)
    x_train ,x_test, y_train ,y_test = train_test_split(x,y,random_state=42)
    clf.fit(x_train,y_train)
    pickle.dump(clf,open('class.sav','wb'))
    print(f'the score is {clf.score(x_test,y_test)}')
