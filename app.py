import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px
from functions import *
@st.cache_data
def load_data():
    return pd.read_csv('Datasets/combined_dataset.csv')
df = load_data()
st.set_page_config(page_title="Fishing Fleet Tracker",page_icon=":sailboat:", layout="wide")
st.title("Fishing Fleet Tracker")
st.space()
"""
This is an analysis of "Monthly Fishing Fleet 2024" datastets provided by the [**Global Fishing Watch.**](https://globalfishingwatch.org/)


The datasets contains information about fishing vessels, the month the data was taken,  their location, country of origin, geartype used for fishing, time spent on water and the number of vessels in the fleet(mmsi present). 
The goal of this project is to analyze the data to identify patterns and trends in fishing activities around the world.
"""
st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Total Vessels", f"{df['mmsi_present'].sum():,}")
col2.metric("Countries Tracked", df['flag'].nunique())
col3.metric("Gear Types", df['geartype'].nunique()) 

"""## Graphical Analysis"""

cols1 = st.columns(3)

left_cell1 = cols1[0].container(
    border=True, height="stretch", vertical_alignment="center"
)
with left_cell1:
    st.subheader("Distribution of Vessels by Country")
    st.space("medium")
    st.space("small")
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
    st.plotly_chart(fig,width='stretch)

mon = st.container(
    border=True, height="stretch", vertical_alignment="center"
)
with mon:
    st.subheader("Vessel Activity by Month")
    con = st.selectbox('Select Country ',flag_list,key='month')
    if con == 'ALL':
        monthly_data = df.groupby('month')['mmsi_present'].sum().reset_index()
    else:
        monthly_data = df[df['flag']==con].groupby('month')['mmsi_present'].sum().reset_index()
    fig = px.line(monthly_data, x='month', y='mmsi_present')
    st.plotly_chart(fig)    

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
    data = get_data(country,gtype,act,month_map[month])
    print(len(data.index))
    if len(data.index) > 100000 :
        data = data.sample(n=100_000, random_state=42)
    fig = px.density_map(data,lat='lat',lon='lon',z='mmsi_present',radius=10,zoom=1,title='Vessel Density Map',color_continuous_scale='inferno')
    st.plotly_chart(fig)

st.space()
"""## Globe Visulization"""

cols3 = st.columns([1,3])
 
left_cell3 = cols3[0].container(
    border=True,height="stretch",vertical_alignment="center"
)
with left_cell3:
    country = st.selectbox('Select country/flag',flag_list2,key='eventchoice7')
    gtype = st.selectbox('Select geartype',gear_list,key='eventchoice8')
    act = st.selectbox('Select Activity',['Both','Loitering','Non Loitering'],key='eventchoice9')
    month = st.selectbox('Select Month',['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec','All'],key='eventchoice10')
    month_map = {"All":'all','Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
right_cell3 = cols3[1].container(
    border=True,height="stretch",vertical_alignment="center"
)
with right_cell3:
    print(country,gtype,act,month_map[month])
    data = get_data(country,gtype,act,month_map[month])
    print(len(data.index))
    if len(data.index) > 100000 :
        data = data.sample(n=100_000, random_state=42)
    data_records = data[['lon', 'lat', 'mmsi_present', 'flag', 'geartype']].to_dict(orient='records')
    deck = globe_plot(data_records)
    html = deck.to_html(as_string=True)
    components.html(html,height=600,scrolling=False)

f_region = st.container(
    border=True,height="stretch",vertical_alignment="center"
)
with f_region:
    st.subheader("Top Fishing Regions")
    df_region = pd.read_csv('Datasets/regions.csv').reset_index(drop=True)
    df_region.sort_values('Vessels',ascending=False,inplace=True)
    st.dataframe(df_region,hide_index=True)

r_data = st.container(
    border=True,height="stretch",vertical_alignment="center"
)
with r_data:
    st.subheader("Raw Data")
    st.dataframe(df.sample(n=1000, random_state=42))
