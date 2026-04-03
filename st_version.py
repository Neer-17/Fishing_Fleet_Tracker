import streamlit as st
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
## Part I: Data Transformation

The package contained twleve datasets of twelve months with each having around 10 million records, 
this is a significantly large size so the datasets were shortned on the basis of the time spent on water,
the datasets contains records only where time spent is greater than equal to 5 hours.
This significantly reduced the size of all datasets making it easy to efficiently work on them.
"""
st.image("Datasets\dataset_size.png",caption="Size Difference")