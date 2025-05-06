import streamlit as st
from read_data import read_data
from kpis import basic_statistics, data_table
from charts import average_score_location, advanced_filtering #plot_filter_country,
import plotly.express as px

df = read_data()

def layout():
    st.markdown("# Executive dashboard")
    
    st.markdown("## Basic statistics")
    
    st.write("Total unique number of:")
    
    labels = ("Records", "Locations", "Subjects", "Timeperiods")

    cols = st.columns(4)

    kpis = basic_statistics()

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)
            
    st.markdown("## Data Table")
    data_table()
    
    st.markdown("## Bar chart showing average PISA scores by location")
    average_score_location()
    
    st.markdown("## Filtering bar chart")
    # plot_filter_country()
    
    
    advanced_filtering()
    # - more interactive filtering to drill down to specific locations, time period, subjects, ... 
    # - this filtering should be displayed on a side panel

if __name__ == "__main__":
    layout()