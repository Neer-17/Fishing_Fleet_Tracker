import streamlit as st
import pandas as pd
import plotly.express as px
from functions import *
st.set_page_config(page_title="Fishing Fleet Tracker",page_icon=":fishing_boat:", layout="wide")
st.title("Fishing Fleet Tracker")
st.space()
"""
This is an analysis of "Monthly Fishing Fleet 2024" datastets provided by the [**Global Fishing Watch.**](https://globalfishingwatch.org/)


The datasets contains information about fishing vessels, the month the data was taken,  their location, country of origin, geartype used for fishing, time spent on water and the number of vessels in the fleet(mmsi present). 
The goal of this project is to analyze the data to identify patterns and trends in fishing activities around the world.
"""
st.space()

"""## Graphical Analysis"""

cols1 = st.columns(3)

left_cell1 = cols1[0].container(
    border=True, height="stretch", vertical_alignment="center"
)
with left_cell1:
    st.subheader("Distribution of Vessels by Country")
    data = country_dis()
    fig = px.pie(data,values=data.values,names=data.index)
    st.plotly_chart(fig,use_container_width=True)

center_cell1 = cols1[1].container(
    border=True, height="stretch", vertical_alignment="center"
)
with center_cell1:
    st.subheader("Distribution of Vessels by Activity")
    chosen_country = st.selectbox('Select country/flag',flag_list,key='eventchoice1')
    flag = chosen_country
    data = activity_dis(flag)
    fig = px.pie(data,values=data.values,names=['Loitering','Non-Loitering'])
    st.plotly_chart(fig,use_container_width=True)

right_cell1 = cols1[2].container(
    border=True,height="stretch",vertical_alignment="center"
)
with right_cell1:
    st.subheader("Distribution of Vessels by Geartype")
    chosen_country = st.selectbox('Select country/flag',flag_list,key='eventchoice2')
    flag = chosen_country
    data = geartype_dis(flag)
    fig = px.pie(data,values=data.values,names=data.index)
    st.plotly_chart(fig,use_container_width=True)

"""## Heatmap"""

cols2 = st.columns([1,3])

left_cell2 = cols2[0].container(
    border=True,height="stretch",vertical_alignment="center"
)
with left_cell2:
    country = st.selectbox('Select country/flag',flag_list2,key='eventchoice3')
    gtype = st.selectbox('Select geartype',gear_list,key='eventchoice4')
    act = st.selectbox('Select Activity',['Both','Loitering','Non Loitering'],key='eventchoice5')
    month = st.selectbox('Select Month',['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec','All'],key='eventchoice6')
    month_map = {"All":'all','Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
right_cell2 = cols2[1].container(
    border=True,height="stretch",vertical_alignment="center"
)
with right_cell2:
    print(country,gtype,act,month_map[month])
    data = density_df(country,gtype,act,month_map[month])
    print(len(data.index))
    if len(data.index) > 100000 :
        data = data.sample(n=100_000, random_state=42)
    fig = px.density_map(data,lat='lat',lon='lon',z='mmsi_present',radius=10,zoom=1,title='Vessel Density Map',color_continuous_scale='inferno')
    st.plotly_chart(fig)

st.space()
"""## Globe"""
