import streamlit as st
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

"""
## Graphical Analysis
"""
fig = geartype_dis('all')
st.pyplot(fig,width="content")