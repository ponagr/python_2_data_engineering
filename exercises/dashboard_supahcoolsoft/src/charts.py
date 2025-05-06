import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from read_data import read_data
import streamlit as st

df = read_data()

def employees_departments_bar_chart():
    employees_departments = df["Department"].value_counts().reset_index(name="Total Employees")
    employees_departments
    fig = px.bar(employees_departments,y="Total Employees", x="Department")
    
    st.plotly_chart(fig)
    

def salary_distribution():
    fig = px.histogram(df, x="Salary_SEK")
    fig.update_layout(
        xaxis_title="Salary", 
        yaxis_title="Employees" 
    )
    st.plotly_chart(fig)
    

def salary_department_boxplot():
    fig = px.box(df, y="Department", x="Salary_SEK", labels={"Salary_SEK": "Salary"})
    st.plotly_chart(fig)
    

def age_distribution():
    fig = px.histogram(df, x="Age")
    fig.update_layout(
            yaxis_title="Employees"
        )
    st.plotly_chart(fig)
    

def age_department_boxplot():
    fig = px.box(df,y="Age", x="Department")
    st.plotly_chart(fig)