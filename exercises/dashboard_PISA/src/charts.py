import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from read_data import read_data
import streamlit as st

df = read_data()

def average_score_location():
    avg_scores = df.groupby("LOCATION")["Value"].mean().reset_index(name="AVG SCORE")

    fig = px.bar(avg_scores, x="LOCATION", y="AVG SCORE")
    st.plotly_chart(fig)
    

# def plot_filter_country():
#     filtered = st.selectbox("Filter by country",df["LOCATION"].unique())
#     filtered_df = df[df["LOCATION"] == filtered]
#     x_axis = st.selectbox("X Axis", ["TIME", "INDICATOR", "Value"])
#     y_axis = st.selectbox("Y Axis", ["Value", "INDICATOR", "TIME"])
    
#     st.markdown(f"### bar chart for {filtered}, comparing {y_axis} and {x_axis}")
    
    
#     fig = px.bar(filtered_df,x=x_axis,y=y_axis, color="SUBJECT", barmode="group")
#     st.plotly_chart(fig)
    

def advanced_filtering():
    # - more interactive filtering to drill down to specific locations, time period, subjects, ... 
    # - this filtering should be displayed on a side panel
    filtered_column = st.selectbox("Filter by",df.columns.unique())
    
    filtered = st.sidebar.selectbox(f"Choose specific {filtered_column}",df[filtered_column].unique())
    
    filtered_df = df[df[filtered_column] == filtered]
    
    x_axis = st.selectbox("X Axis", ["TIME", "INDICATOR", "Value"])
    
    y_axis = st.selectbox("Values", ["Value", "INDICATOR", "TIME"])
    
    st.markdown(f"### bar chart for {filtered}, comparing {y_axis} and {x_axis}")
    
    # filtered_df_2 = filtered_df[y_axis].unique()
    
    # # st.sidebar(f"{}")   
    
    fig = px.bar(filtered_df,x=x_axis,y=y_axis, color="SUBJECT", barmode="group")
    st.plotly_chart(fig)