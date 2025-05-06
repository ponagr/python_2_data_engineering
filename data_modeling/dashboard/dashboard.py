from pathlib import Path
import os
import pandas as pd
import duckdb
import streamlit as st
import matplotlib.pyplot
import plotly.express as px

# working_directory = Path(__file__).parents[1]
# os.chdir(working_directory)

# with duckdb.connect("ads_data_warehouse.duckdb") as con:
#     df = con.execute("SELECT * FROM mart.mart_job_ads").df()
#     df_healthcare = con.execute("SELECT * FROM mart.mart_hälso_sjukvård").df()
#     df_education = con.execute("SELECT * FROM mart.mart_pedagogik").df()
#     df_technical = con.execute("SELECT * FROM mart.mart_teknisk_inriktning").df()

def group_by_city(df):
    return df.groupby("workplace_municipality")["vacancies"].sum().reset_index(name="total vacancies").sort_values("total vacancies", ascending=False).reset_index(drop=True)

def group_by_occupation(df):
    return df.groupby("occupation")["vacancies"].sum().reset_index(name="total vacancies").sort_values("total vacancies", ascending=False).reset_index(drop=True)

# skicka in "occupation" eller "workplace_city" eller någon annan kolumn via df.columns.unique()
def group_with_vacancies(df, column):
    return df.groupby(column)["vacancies"].sum().reset_index(name="total vacancies").sort_values("total vacancies", ascending=False).reset_index(drop=True)

# funktion för att sålla ut efter en specifik stad

def show_metrics(df:pd.DataFrame, metric_labels:str, metric_kpis:str, metric_amount:int):
    """Function for generating metrics 

    Args:
        df (dataframe): dataframe to filter metrics from
        metric_labels (str): string for metric labels using df["metric_labels"] to filter out label values from df
        metric_kpis (str): string for metric kpis using df["metric_kpis"] to filter out kpi values from df
        metric_amount (int): integer for amount of metric columns to use
    """
    labels = df[metric_labels].head(metric_amount)
    cols = st.columns(metric_amount)
    kpis = df[metric_kpis].head(metric_amount)

    for col, label, kpi in zip(cols, labels, kpis):
        with col: 
            st.metric(label=label, value=kpi)

def layout():
    st.markdown("# Job ads dashboard")
    
    
    field_vacancies = df_full.groupby("occupation_field")["vacancies"].sum().reset_index(name="total vacancies").sort_values("total vacancies", ascending=False).reset_index(drop=True)
    
    st.markdown("## Total vacancies per work field")
    show_metrics(field_vacancies, "occupation_field", "total vacancies", 3)
    
    field = st.selectbox("Select work field", df_full["occupation_field"].unique())
    
    # filtrera på field
    st.markdown("## Top 5 citys with the most vacancies")
    show_metrics(df_city, "workplace_municipality", "total vacancies", 5)
    
    city = st.selectbox("Select city", df_city["workplace_municipality"].unique())
    
    fig = px.bar(
            df_city.head(15),
            x="workplace_municipality",
            y="total vacancies",
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )
    st.plotly_chart(fig)
    
    # visa experience required körkort osv för valda fältet
    
    # filtrera vidare på workplace_group eller 
    
    # columns:
    #   ['occupation_id', 'job_details_id', 'employer_id',
    #    'auxillary_attributes_id', 'vacancies', 'relevance',
    #    'application_deadline', 'occupation_id_1', 'occupation',
    #    'occupation_group', 'occupation_field', 'job_details_id_1', 'headline',
    #    'description', 'description_html', 'duration', 'salary_type',
    #    'salary_description', 'working_hours_type', 'scope_of_work_min',
    #    'scope_of_work_max', 'employer_id_1', 'employer_name',
    #    'employer_workplace', 'employer_organization_number',
    #    'workplace_street_address', 'workplace_region', 'workplace_postcode',
    #    'workplace_municipality', 'workplace_city', 'workplace_country',
    #    'auxillary_attributes_id_1', 'experience_required', 'driver_licence',
    #    'access_to_own_car'],
    # metrics:
        # top 5 städer med lediga jobb
        # tex top 5 jobbtyper inom en specifik work_field för en specifik workplace_city baserat på vacancies
        # hur många totala jobb för varj fält för en specifik stad
    # från df_full - totalt antal jobb för varje yrkesgrupp, totalt antal jobb per stad, 
    


if __name__ == "__main__":
    working_directory = Path(__file__).parents[1]
    os.chdir(working_directory)
    
    with duckdb.connect("ads_data_warehouse.duckdb") as con:
        df_full = con.execute("SELECT * FROM mart.mart_job_ads").df()
        df_healthcare = con.execute("SELECT * FROM mart.mart_hälso_sjukvård").df()
        df_education = con.execute("SELECT * FROM mart.mart_pedagogik").df()
        df_technical = con.execute("SELECT * FROM mart.mart_teknisk_inriktning").df()
    
    df_city = group_by_city(df_full)
    layout()
    # print(df_healthcare["occupation_field"])
    # print(df_education["occupation_field"])
    # print(df_technical["occupation_field"])