# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 01:25:40 2021

@author: Elizabeth Shi
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("Elizabeth's version of Streamlit")

df_Hospital = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
df_Outpatient = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
df_Inpatient =pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

st.dataframe(df_Hospital)