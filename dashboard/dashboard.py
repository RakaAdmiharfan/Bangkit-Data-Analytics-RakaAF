import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

season_mapping = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}
day_df=pd.read_csv("day.csv")
hour_df=pd.read_csv("hour.csv")
needed_columns = ['season', 'cnt']
filtered_day_df = day_df[needed_columns]
needed_columns = ['season', 'hr', 'cnt']
filtered_hour_df = hour_df[needed_columns]



st.title('Visualisasi Data Berdasarkan Pertanyaan Bisnis')


st.subheader('Mean Count by Season')
result_day = filtered_day_df.groupby(by="season").agg({
    "cnt": ["mean"]
})
result_day.index = result_day.index.map(season_mapping)
result_day.columns = result_day.columns.droplevel(0)
st.bar_chart(result_day[('mean')])


st.subheader('Mean Count by Hour in Season Fall')
result_hour = filtered_hour_df.groupby(by="hr").agg({
    "cnt": ["mean"]
})
result_hour_sorted = result_hour.sort_values(by=('cnt', 'mean'), ascending=False)
result_hour_sorted.columns = result_hour_sorted.columns.droplevel(0)

st.bar_chart(result_hour_sorted['mean'])

