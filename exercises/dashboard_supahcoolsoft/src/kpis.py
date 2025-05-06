from read_data import read_data
import streamlit as st
import pandas as pd


df = read_data()

# - basic statistics on employees (total count, average age, average salary)
def employee_stats():
    total_employees = len(df)
    avg_age = df["Age"].mean()
    avg_salary = df["Salary_SEK"].mean()
    
    return int(total_employees), int(avg_age), int(avg_salary)


# - show a table with employee details
def employee_details_table():
    df_employee_details = {
        "Name": df["FirstName"] + " " + df["LastName"],
        "Age": df["Age"],
        "Department": df["Department"],
        "Position": df["Position"],
        "Email": df["Email"],
        "PhoneNumber": df["PhoneNumber"]
    }
    df_employee_details = pd.DataFrame(df_employee_details)

    st.dataframe(df_employee_details)