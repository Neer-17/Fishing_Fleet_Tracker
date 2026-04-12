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

def v_dis():
    data = country_dis()
    fig = px.pie(data,values=data.values,names=data.index)
    st.plotly_chart(fig,use_container_width=True)

def a_dis(flag):
    data = activity_dis(flag)
    fig = px.pie(data,values=data.values,names=data.index)
    st.plotly_chart(fig,use_container_width=True)

cols = st.columns([1,3])


top_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)
with top_left_cell:
    select_event = st.selectbox('Charts',
                                    ['Vessel Distribution','Country wise Vessel activity','Counrty wise Vessels Geartype'], key='datatype')
    if select_event == 'Country wise Vessel activity':
        choose_country = st.selectbox('Select country/flag',flag_list,key='eventchoice')
        flag = choose_country
        data = activity_dis(flag)
        fig = px.pie(data,values=data.values,names=['Not Loitering','Loitering'])
    elif select_event == 'Vessel Distribution':
        data = country_dis()
        fig = px.pie(data,values=data.values,names=data.index)
    elif select_event == 'Counrty wise Vessels Geartype':
        choose_country = st.selectbox('Select country/flag',flag_list,key='eventchoice')
        flag = choose_country
        data = geartype_dis(flag)
        fig = px.pie(data,values=data.values,names=data.index)


right_cell = cols[1].container(
    border=True, height="stretch", vertical_alignment="center"
)
with right_cell:
    st.plotly_chart(fig)