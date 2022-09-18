from numpy import random
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from .models import Schedule
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import datetime
from dateutil import tz
import pickle

timezone = tz.gettz('Asia/Tokyo')

def type_model_data():
    x = pd.DataFrame()
    y = pd.DataFrame([int(ele.schedule_class) for ele in data_obj])
    x['year'] = [int(ele.start_date.year) for ele in data_obj]
    x['month'] = [int(ele.start_date.month) for ele in data_obj]
    x['day'] =[int(ele.start_date.day) for ele in data_obj]
    x['hour'] = [int(ele.start_date.hour) for ele in data_obj]
    x['minute'] = [int(ele.start_date.minute) for ele in data_obj]
    return x,y

def end_model_data():
    data_x, _ =type_model_data()
    y = pd.DataFrame([datetime.datetime.timestamp(ele.end_date)*1000 for ele in data_obj])
    data_x['schedule_type'] = [int(ele.schedule_class) for ele in data_obj]
    x = pd.get_dummies(data_x,columns=['schedule_type'])
    return x,y

def clasifyer(start,end):
    clf_end = pickle.load(open('endtime.sav','rb'))
    clf_type = pickle.load(open('schedule_type','rb'))
    start_time = datetime.datetime.strptime(start,r"%d/%m/%Y %H:%M:%S")
    plan_ls = []
    limit = datetime.datetime.timestamp(datetime.datetime.strptime(end,r"%d/%m/%Y %H:%M:%S"))
    while datetime.datetime.timestamp(start_time) <= limit:
        x = pd.DataFrame({'year':start_time.year,'month':start_time.month,'day':start_time.day,'minute':start_time.minute})
        schedule_type = clf_type.predict(x)
        x['schedule_type'] =schedule_type
        end_time = datetime.datetime.fromtimestamp(clf_end.predict(x),timezone)
        if schedule_type != 1:
            if end_time <= limit:
                plan_ls.append([start_time,end_time,str(schedule_type)])
            else:
                plan_ls.append([start_time,limit,str(schedule_type)])
        start_time = end_time
    return plan_ls



if __name__ == '__main__':
    data_obj = Schedule.objects.all()
    clf_type = RandomForestClassifier(n_estimators=1,random_state=42)
    x, y = type_model_data()  #x=start,user_class y=schedule_type
    x_train, x_test, y_train , y_test = train_test_split(x,y)
    clf_type.fit(x_train,y_train)
    pickle.dump(clf_type,open('schedule.sav','wb'))
    print(f'the score of type_model is {clf_type.score(x_test,y_test)}')
    clf_end = SVC()
    x, y = end_model_data()
    x_train, x_test, y_train , y_test = train_test_split(x,y)
    clf_end.fit(x_train,y_train)
    pickle.dump(clf_end,open('endtime.sav','wb'))
    print(f'the score of end_model is {clf_end.score(x_test,y_test)}')
