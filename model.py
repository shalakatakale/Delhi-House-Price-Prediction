#Import Libraries
import numpy as np
import pandas as pd
import joblib
 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
 
#load data
df = pd.read_csv("ReadytoUse.csv")
 
# Split data
X= df.drop('Price', axis=1)
y= df['Price']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42)
 
# Feature Scaling
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Load Model
model = joblib.load('House_price_prediction.pkl')

def predict_house_price(BHK,Bathroom,Parking,Area,Per_Sqft,Furnishing,Status,Transaction,Type,Locality):
    x =np.zeros(len(X.columns)) 
    #print(x)
    x[0]=BHK
    x[1]=Bathroom
    x[2]=Parking
    x[3]=Area
    x[4]=Per_Sqft
    
    if "Furnishing" == "Semi-Furnished":
        x[5] = 1
    elif "Furnishing" == "Unfurnished":
        x[5] = 2
    elif "Furnishing" == "Furnished":
        x[5] = 0
        
    if "Status" == "Ready_to_move":
        x[6] = 1
    elif "Status" == "Almost_ready":
        x[6] = 0
    
    if "Transaction" == "New_Property":
        x[7] = 0
    elif "Transction" == "Resale":
        x[7] = 1
    
    if "Type" == "Builder_Floor":
        x[8] = 1
    elif "Type" == "Apartment":
        x[8] = 0
        
    if "Locality_"+Locality in X.columns:
        Locality_index = np.where(X.columns=="Locality_"+Locality)[0][0]
        x[Locality_index] =1
        
        
    # feature scaling
    x = scaler.transform([x]) # give 2d np array for feature scaling and get 1d scaled np array
    return model.predict(x)[0]


# predict_house_price(model=model,BHK=2,Bathroom=2,Parking=2,Area=1000,Per_Sqft=8667,\
# Furnishing="Unfurnished",Status="Ready_to_move", Transaction="Resale",\
# #  Type="Apartment",Locality="New Friends Colony")