import streamlit as st
from read_data import read_data
from kpis import employee_stats, employee_details_table
from charts import employees_departments_bar_chart, salary_distribution, salary_department_boxplot, age_distribution, age_department_boxplot

df = read_data()

def layout():
    st.markdown("# Executive dashboard")
    
    st.markdown("## Basic employee statistics")
    
    labels = ("total employees", "average age", "average salary")

    cols = st.columns(3)

    kpis = employee_stats()

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)
            

    st.markdown("## Employee details")
    employee_details_table()
    
    st.markdown("## Number of employees accross departments")
    
    employees_departments_bar_chart()
    
    st.markdown("## Employee salary distribution")
    salary_distribution()
    
    st.markdown("## Salary for each department")
    salary_department_boxplot()
    
    st.markdown("## Age distribution")
    age_distribution()
    
    st.markdown("## Age distribution for each department")
    age_department_boxplot()

if __name__ == "__main__":
    layout()