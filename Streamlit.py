# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 01:25:40 2021

@author: Elizabeth Shi
"""
conda install streamlit
import streamlit as st
import pandas as pd
import numpy as np
conda install sweetviz
import sweetviz
import sweetviz as sv
conda install pandas_profiling

import matplotlib.pyplot as plt
import seaborn as sns

conda install pyjanitor
from janitor import clean_names, remove_empty

import os
import glob


# Cleaning of Hospital Table
df_Hospital = pd.DataFrame.from_dict(df_Hospital)
df = clean_names(df_Hospital)
df = remove_empty(df_Hospital)

display(df_Hospital)

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

df_merged1

df_merged2

df_merge1_clean = df_merged1[df_merged1['hospital_name'].notna()]

df_merge2_clean = df_merged2[df_merged2['hospital_name'].notna()]

df_merge1_clean

df_merge2_clean

df_merged_clean_SB = df_merge1_clean[df_merge1_clean['hospital_name']=='SUNY/STONY BROOK UNIVERSITY HOSPITAL']
df_merged_clean_SB

df_merged_clean_SB2 = df_merge2_clean[df_merge2_clean['hospital_name']=='SUNY/STONY BROOK UNIVERSITY HOSPITAL']
df_merged_clean_SB2

# Streamlit

st.title("Elizabeth's version of Streamlit")

df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
df_Outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
df_Inpatient =pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

st.header( '2015 Hospital Table')
st.dataframe(df_Hospital)
st.header('2015 Inpatient Table')
st.dataframe(df_Inpatient)
st.header('2015 Outpatient Table')
st.dataframe(df_Outpatient)

# question 1
st.title('How Does Stony Brook Compare To The Rest of NY')
st.header('Hospital and Outpatient')
df_merged_clean_NY = df_merge1_clean[df_merge1_clean['provider_state']=='NY']
df_merged_clean_NY
Pivot_table_NY = df_merged_clean_NY.pivot(index="provider_name", columns= 'apc' ,values ='average_estimated_submitted_charges')
Pivot_table_NY_sample = Pivot_table_NY.sample(10)
pivot_table_sb = df_merged_clean_SB.pivot(index="provider_name", columns= 'apc' ,values ='average_estimated_submitted_charges')
pivot_table_sb 
st.subheader('NY Pivot Table')
st.dataframe(Pivot_table_NY_sample)
st.subheader('SB Pivot Table')
st.dataframe(pivot_table_sb)