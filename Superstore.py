#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:04:28 2021

@author: davidbroxmeyer 
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Superstore Data")

@st.cache
def load_data(nrows = 1000):
    df = pd.read_csv('https://raw.githubusercontent.com/davidbroxmeyer/SuperstoreFinal/main/US%20Superstore%20data%20Transformed.csv', nrows = 1000)

    return df


nrows = st.sidebar.number_input("Number of Rows to Load",min_value = 1000, max_value = 10000, step = 1000)

df = load_data(nrows)

x_axis = st.sidebar.selectbox('Choose Your X-Axis Category', df.select_dtypes(include=np.object).columns, index = 3)
    
y_axis = st.sidebar.selectbox('Choose Your Y-Axis Category', df.select_dtypes(include=np.number).columns, index = 1)
    
chart_type = st.sidebar.selectbox('Choose Your Chart Type', ['table', 'line', 'bar', 'strip'])
    
@st.cache
    
def create_grouping(x_axis, y_axis):
    grouping =  df.groupby(x_axis)[y_axis].sum()
    return grouping
    
grouping = create_grouping(x_axis, y_axis)
    
st.write(df)
    
st.title("Grouped Data")
    
if chart_type == 'line':
    st.line_chart(grouping)
elif chart_type == 'table':
    st.write(grouping)
elif chart_type == 'bar':
    st.bar_chart(grouping)
else:
    st.plotly_chart(px.strip(df[[x_axis, y_axis]][:100], x = x_axis, y = y_axis))
        

    
