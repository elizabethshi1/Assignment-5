# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 01:25:40 2021

@author: Elizabeth Shi
"""



import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time

df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
df_Outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
df_Inpatient =pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')





#SBU

SB_Hospital = df_Hospital[df_Hospital['provider_id']== '330393']
SB_Inpatient = df_Inpatient[df_Inpatient['provider_id']== '330393']
SB_Outpatient = df_Outpatient[df_Outpatient['provider_id']== '330393']

#merge tables

df_Hospital['provider_id'] = df_Hospital['provider_id'].astype(str)
df_Outpatient['provider_id'] = df_Outpatient['provider_id'].astype(str)
df_Inpatient['provider_id'] = df_Inpatient['provider_id'].astype(str)

df_merged1 = df_Outpatient.merge(df_Hospital, how= 'left', left_on='provider_id', right_on='provider_id')

df_merged2 = df_Inpatient.merge(df_Hospital, how= 'left', left_on='provider_id', right_on='provider_id')

len(df_merged1)



df_merge1_clean = df_merged1[df_merged1['hospital_name'].notna()]

df_merge2_clean = df_merged2[df_merged2['hospital_name'].notna()]


df_merged_clean_SB = df_merge1_clean[df_merge1_clean['hospital_name']=='SUNY/STONY BROOK UNIVERSITY HOSPITAL']


df_merged_clean_SB2 = df_merge2_clean[df_merge2_clean['hospital_name']=='SUNY/STONY BROOK UNIVERSITY HOSPITAL']


# Streamlit

st.title("Elizabeth's version of Streamlit")


st.header( '2015 Hospital Table')
st.dataframe(df_Hospital)
st.header('2015 Inpatient Table')
st.dataframe(df_Inpatient)
st.header('2015 Outpatient Table')
st.dataframe(df_Outpatient)

pie1 = pd.DataFrame(df_merge1_clean['provider_state'].value_counts().reset_index())
st.dataframe(pie1)
st.header("Pie Chart of Outpatient's and Hospital's States")
fig = px.pie(pie1, values='provider_state',names='index')
st.plotly_chart(fig)

st.header("bar Chart of NY Hospital Type")
df_hospital_NY= df_Hospital[df_Hospital['provider_state']=='NY']
bar1 = df_hospital_NY['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)


# question 1
st.title('How Does Stony Brook Compare To The Rest of NY')
st.header('Hospital and Outpatient')
df_merged_clean_NY = df_merge1_clean[df_merge1_clean['provider_state']=='NY']
df_merged_clean_NY
Pivot_table_NY = df_merged_clean_NY.pivot(index="provider_name", columns= 'apc' ,values ='average_estimated_submitted_charges')
Pivot_table_NY_sample = Pivot_table_NY.sample(10)
pivot_table_sb = df_merged_clean_SB.pivot(index="provider_name", columns= 'apc' ,values ='average_estimated_submitted_charges') 
st.subheader('NY Pivot Table')
st.dataframe(Pivot_table_NY_sample)
st.subheader('SB Pivot Table')
st.dataframe(pivot_table_sb)
