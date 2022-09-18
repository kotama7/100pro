from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler

def cleansing(data:pd.DataFrame):
    x_data = data['x_data']
    y_data = data['y_data']
    x = pd.DataFrame()
    y = pd.DataFrame([int(ele) for ele in y_data])
    for i in range(100):
        x[i] = [ord(ele.ljust(100)[i]) for ele in x_data]
    return x,y

def classifyer(detail:str):
    clf = pickle.load(open('class.sav','rb'))
    scalar = pickle.load(pickle.dump(open('forest_scalar.sav','wb')))
    x = pd.DataFrame([ord(ele) for ele in detail.ljust(100)])
    x = scalar.transform(x)
    ans = clf.predict(x)
    return str(ans)

if __name__ == '__main__':
    clf = RandomForestClassifier(n_estimators=2)
    data = pd.read_csv('./dataset_detail.csv')
    x,y = cleansing(data)
    x_train ,x_test, y_train ,y_test = train_test_split(x,y,random_state=42)
    scalar  = MinMaxScaler().fit(x_train)
    x_train = scalar.transform(x_train)
    x_test = scalar.transform(x_test)
    clf.fit(x_train,y_train)
    pickle.dump(clf,open('class.sav','wb'))
    pickle.dump(scalar,open('forest_scalar.sav','wb'))
    print(f'the score is {clf.score(x_test,y_test)}')
