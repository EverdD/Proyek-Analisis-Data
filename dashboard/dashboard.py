import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Setting up helper functions for the dataframe
def create_area_df(df):
    area_df = df.groupby("column_station").index_AQI.sum().sort_values(ascending=False).reset_index()
    return area_df

def create_Vclimate_mean_df(df):
    Vclimate_mean_df = df.groupby(by="air_quality").agg({
        "column_TEMP": ['mean'],
        "column_PRES": ['mean'],
        "column_DEWP": ['mean'],
        "column_WSPM": ['mean']
    })
    Vclimate_mean_df = Vclimate_mean_df.T # Firman Nurcahyo_DICODING_IDCAMP
    return Vclimate_mean_df

def create_df_time(df):
    df_time = df
    return df_time

# Prepare dataset
df_AQI = pd.read_csv("dashboard/df_AQI.csv")
df_AQI.sort_values(by="column_datetime", inplace=True)
df_AQI.reset_index(drop=True, inplace=True)
df_AQI["column_datetime"] = pd.to_datetime(df_AQI["column_datetime"])

# Data filters
min_date = df_AQI["column_datetime"].min()
max_date = df_AQI["column_datetime"].max()

with st.sidebar:
    # Gets start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df_AQI[(df_AQI["column_datetime"] >= str(start_date)) & 
                (df_AQI["column_datetime"] <= str(end_date))]

area_df = create_area_df(main_df)
Vclimate_mean_df = create_Vclimate_mean_df(main_df)
time_df = create_df_time(main_df)

# Create dashboard header
st.header('Air Quality Index dashboard :cloud:')

# Visualizing Best & Worst Air Quality Index (AQI)
st.subheader("Best & Worst Air Quality Index (AQI)")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors1 = ["#00FF00", "#D3D3D9", "#D3D3D9", "#D3D3D9", "#D3D3D9"]
colors2 = ["#1E90FF", "#D3D3D9", "#D3D3D9", "#D3D3D9", "#D3D3D9"]

sns.barplot(x="index_AQI", y="column_station", data=area_df.head(5), palette=colors1, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Air Quality Index (AQI)", loc="center", fontsize=30)
ax[0].tick_params(axis='y', labelsize=20)
ax[0].tick_params(axis='x', labelsize=20) # Firman Nurcahyo_DICODING_IDCAMP

sns.barplot(x="index_AQI", y="column_station", data=area_df.sort_values(by="index_AQI", ascending=True).head(5), palette=colors2, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Air Quality Index (AQI)", loc="center", fontsize=30)
ax[1].tick_params(axis='y', labelsize=20)
ax[1].tick_params(axis='x', labelsize=20)

st.pyplot(fig)

# Visualizing Average climate Variables
st.subheader("Average climate Variables") # Firman Nurcahyo_DICODING_IDCAMP

# Metrics for each variable
col1, col2, col3, col4 = st.columns(4)

with col1:
    mean_temp = round(Vclimate_mean_df.T.column_TEMP.mean(), 2)
    st.metric("Average TEMP", value=mean_temp)

with col2:
    mean_pres = round(Vclimate_mean_df.T.column_PRES.mean(), 2)
    st.metric("Average PRES", value=mean_pres)

with col3:
    mean_dewp = round(Vclimate_mean_df.T.column_DEWP.mean(), 2)
    st.metric("Average DEWP", value=mean_dewp) # Firman Nurcahyo_DICODING_IDCAMP

with col4:
    mean_wspm = round(Vclimate_mean_df.T.column_WSPM.mean(), 2)
    st.metric("Average WSPM", value=mean_wspm)

# Bar plot for climate Variables
species = ("TEMP", "PRES", "DEWP", "WSPM")
x = np.arange(len(species))
width = 0.25
multiplier = 1

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in Vclimate_mean_df.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=4, rotation=30)
    multiplier += 1

ax.set_ylabel('Mean')
ax.set_title('Impact of TEMP, WSPM, PRES, & DEWP')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=4)
ax.set_ylim(-2, 45)

st.pyplot(fig)

# Visualizing Air Quality Index by Time
st.subheader("Air Quality Index by Time")

col1, col2, col3, col4 = st.columns(4)

with col1:
    max_year = time_df.groupby(by="column_year").index_AQI.sum().idxmax()
    st.metric("Best Year", value=max_year)

with col2:
    max_month = time_df.groupby(by="column_month").index_AQI.sum().idxmax()
    st.metric("Best Month", value=max_month)
# Firman Nurcahyo_DICODING_IDCAMP
with col3:
    max_day = time_df.groupby(by="column_day").index_AQI.sum().idxmax()
    st.metric("Best Day", value=max_day)

with col4:
    max_hour = time_df.groupby(by="column_hour").index_AQI.sum().idxmax()
    st.metric("Best Hour", value=max_hour)

cat_var = ["column_year", "column_month", "column_day", "column_hour"]
fig, ax = plt.subplots(nrows=2, ncols=int(len(cat_var)/2), figsize=(40, 15))

k = 0
for i in range(2):
    for j in range(int(len(cat_var)/2)):
        sns.barplot(y=time_df.groupby(by=cat_var[k]).index_AQI.sum(),
                    x=time_df.groupby(by=cat_var[k]).mean(numeric_only=True).index, ax=ax[i, j], palette='winter')

        ax[i, j].set_title(f'{cat_var[k].upper()}', fontsize=30)
        ax[i, j].set_ylabel('')
        ax[i, j].set_xlabel('')
        ax[i, j].tick_params(axis='y', labelsize=30)
        ax[i, j].tick_params(axis='x', labelsize=25)
        plt.xticks(rotation=315)
        k += 1

st.pyplot(fig)