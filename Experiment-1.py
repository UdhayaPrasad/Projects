import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
import numpy as np

st.title('Insulin Concentration Prediction in Rats')
st.markdown(' Done By Dr.Surendiran B,Udhayaprasad, Shrihari and Ayon Biswas ')

file_upload = st.file_uploader("Choose Your File:",type='csv')
if file_upload is not None:
    st.write("File Successfully Uploaded")
    df = pd.read_csv(file_upload)

    st.subheader('Dataset Overview')
    st.write(df.head())

    st.subheader('Dataset Summary')
    st.write(df.describe())

    
    st.subheader('Checking Null Values')
    st.write(df.isnull().sum())

    st.subheader('No of Rows and Columns')
    st.write(df.shape)

    df = df.drop(columns=['Animal ID','Group','Timepoint (min)'])

    st.subheader('Bar Chart')
   
    st.bar_chart(df)

    st.subheader("Scatter Plot") 
    
    st.scatter_chart(df)

    st.subheader("Area Chart")
    st.area_chart(df)
    
    x = df.drop(columns='Insulin (ng/mL)')
    y = df['Insulin (ng/mL)']

    test_val = st.selectbox("Select the Testing Data Value in Percentage",(0.1,0.2,0.3))
    if(test_val ==0.1):
        st.write('You Choosed Training Data as 90% and Testing Data as 10%') 

    elif(test_val ==0.2):
        st.write('You Choosed Training Data as 80% and Testing Data as 20%') 

    else:
        st.write('You Choosed Training Data as 70% and Testing Data as 30%') 
    

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_val)

    model = st.selectbox("Choose the Model",('Random Forest','AdaBoost'))
    st.subheader("Predictions Results:")

 

    if(model=='Random Forest'):
        Rmodel = RandomForestRegressor(n_estimators=1000,random_state=42)
        Rmodel.fit(x_train,y_train)
        Predict = Rmodel.predict(x_test) 
        st.subheader('RandomForest:')
        st.write(Predict)
        Mse = mean_squared_error(y_test,Predict)
        st.subheader('Prediction Error')
        st.write("Random Forest:",Mse)

    elif(model=='AdaBoost'):
           Amodel = AdaBoostRegressor(n_estimators=1000,random_state=42)
           Amodel.fit(x_train,y_train)
           Apredict = Amodel.predict(x_test)
           st.subheader('AdaBoost:')
           st.write(Apredict)
           aMSE = mean_squared_error(y_test,Apredict)  
           st.subheader('Prediction Error (MSE)')
           st.write("AdaBoost:",aMSE)  

else:
    st.write("File is not uploaded")
