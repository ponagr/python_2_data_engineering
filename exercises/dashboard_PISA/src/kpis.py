from read_data import read_data
import streamlit as st
import pandas as pd


df = read_data()


def basic_statistics():
    records = len(df)
    locations = df["LOCATION"].nunique()
    subjects = df["SUBJECT"].nunique()
    timeperiods = df["TIME"].nunique()
    
    return records, locations, subjects, timeperiods


def data_table():
    st.dataframe(df)