import matplotlib.pyplot as plt
from read_data import read_data
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, root_mean_squared_error
import numpy as np

df = read_data()

X = df[["Temperature"]]
y = df["Revenue"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
forest_model.fit(X_train,y_train)
forest_y_pred = forest_model.predict(X_test)

forest_mse = mean_squared_error(y_test, forest_y_pred)
forest_r2 = r2_score(y_test, forest_y_pred)
forest_mae = mean_absolute_error(y_test, forest_y_pred)
forest_rmse = root_mean_squared_error(y_test, forest_y_pred)


linear_model = LinearRegression()
linear_model.fit(X_train,y_train)
linear_y_pred = linear_model.predict(X_test)

linear_mse = mean_squared_error(y_test, linear_y_pred)
linear_r2 = r2_score(y_test, linear_y_pred)
linear_mae = mean_absolute_error(y_test, linear_y_pred)
linear_rmse = root_mean_squared_error(y_test, linear_y_pred)

temp_prediction = X_test.round() 
temp_prediction["Predicted Revenue"] = forest_y_pred.round()
temp_prediction = temp_prediction.sort_values(by="Temperature")
    

def prediction_charts():
    fig,ax = plt.subplots(1,2, figsize=(20,8))

    ax[0].scatter(X_train, y_train, label="Training data", color="blue")
    ax[0].scatter(X_test, linear_y_pred, label="Predictions", color="red")
    ax[0].set_title("Linear Regression")
    ax[0].set_xlabel("Temperature")
    ax[0].set_ylabel("Revenue")
    ax[0].legend()

    ax[1].scatter(X_train, y_train, label="Training data", color="blue")
    ax[1].scatter(X_test, forest_y_pred, label="Predictions", color="red")
    ax[1].set_title("Random Forest Regression")
    ax[1].set_xlabel("Temperature")
    ax[1].set_ylabel("Revenue")
    ax[1].legend()
    
    st.pyplot(fig)
    

def linear_metrics():
    labels = ("MSE", "R2", "MAE", "RMSE")

    cols = st.columns(4)

    kpis = (linear_mse, linear_r2, linear_mae, linear_rmse)

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=round(kpi, 2))
            

def forest_metrics():
    labels = ("MSE", "R2", "MAE", "RMSE")

    cols = st.columns(4)

    kpis = (forest_mse, forest_r2, forest_mae, forest_rmse)

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=round(kpi, 2))

def predict_revenue():

    choice = st.number_input("Enter temperature: ")
    
    choice = np.array([[choice]])
    user_choice = forest_model.predict(choice)[0].round(1)

    st.markdown(f"### Expected revenue: {user_choice} SEK")
    

