import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#importing the data

raw_data=pd.read_csv("/home/jay/Documents/code/fruit quality/apple_quality.csv")
data=raw_data.copy()

# maping the data and cleaning

encode=LabelEncoder()
data['Quality']=encode.fit_transform(data['Quality'])
data.dropna(inplace=True)
data.drop('A_id',axis=1,inplace=True)


#Declaring the Independent and Dependent Variables
x=data[['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness' ,'Acidity']]
y=data['Quality']

# Train Test Split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

# Model Creation
clf=RandomForestClassifier(n_estimators=50,min_samples_split=10,min_samples_leaf= 2,max_depth= 20)
clf.fit(x_train,y_train)

