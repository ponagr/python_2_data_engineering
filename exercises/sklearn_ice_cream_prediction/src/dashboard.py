from read_data import read_data
import streamlit as st
from kpis import prediction_charts, predict_revenue, linear_metrics, forest_metrics, temp_prediction

df = read_data()


def layout():
    st.markdown("# Ice Cream Prediction App")
    
    st.markdown("## Choose temperature for prediction")
    predict_revenue()
    
    st.markdown("## Dataframe before predictions")
    
    st.dataframe(df)
    
    st.markdown("## Metrics")
    
    st.markdown("### Linear")
    linear_metrics()
    st.markdown("")
    st.markdown("### Random Forest")
    forest_metrics()
    
    st.markdown("## Prediction chart")
    prediction_charts()
    
    st.markdown("## Dataframe after predictions")
    
    st.dataframe(temp_prediction)
    
    


if __name__ == "__main__":
    layout()