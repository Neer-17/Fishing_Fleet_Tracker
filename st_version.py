import streamlit as st
import pandas as pd
import altair as alt
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


### I : Distribution of Vessels by Country
"""
data = pd.DataFrame(country_dis())
# print(type(data))
base = alt.Chart(data).encode(
    theta=alt.Theta(field="mmsi_present", type="quantitative"),
    color=alt.Color(field="flag", type="nominal", legend=None)
).properties(width=400, height=400)
pie=base.mark_arc(innerRadius=50, stroke="#fff")
text = base.mark_text(radius=120, size=14).encode(
    text=alt.Text(field="mmsi_present", type="quantitative", format=".0f")
)
st.altair_chart(pie + text)
st.space()

