import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datasets/fleet_01.csv')
# df.head()

# df.info()

# df.describe()

# cor = df.corr(numeric_only=True)
# sns.heatmap(cor,annot=True,cmap='coolwarm')
plt.style.use('dark_background')
#Count of Origins of the ships
flag_list = df['flag'].unique()
countries = [country for country in flag_list if len(country)==3]
unknown = [country for country in flag_list if len(country)!=3]
# print("Countries : ",len(countries))
# print("Unokown : ",len(unknown))

#Types of gears used for fishing
gear_list = df['geartype'].unique()
# print("Types of gears : ",len(gear_list))
# print(gear_list)

#Distribution of Vessels by Country
def country_dis():
  most_vessels_by_countries = df.groupby('flag')['mmsi_present'].sum().sort_values(ascending=False).head(9)
  other = df['mmsi_present'].sum() - most_vessels_by_countries.sum()
  most_vessels_by_countries['Other{279 Flags}'] = other
  return most_vessels_by_countries

# Function for distribution of Vessels by Activity
# def activity_dis(country):
#   if country.lower() == 'all':
#     loitering_vessels = df.groupby('loitering')['mmsi_present'].sum()
#   elif country.upper() in flag_list:
#     loitering_vessels = df[df['flag'] == country.upper()].groupby('loitering')['mmsi_present'].sum()
#   else:
#     print('Invalid Country')
#     return
#   print(loitering_vessels)
#   plt.figure(figsize=(12,6))
#   plt.pie(loitering_vessels,labels=['Not Loitering','Loitering'],autopct='%1.1f%%',colors=sns.color_palette('deep'))
#   plt.title(f"Distibution of {country.upper()} Vessels by Activity ")

# activity_dis('all')

# Distibution of Vessels by Geartype
# vessel_dis_by_geartype = df.groupby('geartype')['mmsi_present'].sum()
# print(vessel_dis_by_geartype)
# plt.figure(figsize=(24,6))
# sns.barplot(x=vessel_dis_by_geartype.index,y=vessel_dis_by_geartype.values)
# plt.title(f"Distibution of Vessels by Geartype")

def geartype_dis(country):
  if country.lower() == 'all':
    geartype_vessels = df.groupby('geartype')['mmsi_present'].sum().sort_values(ascending=False).head(5)
    other = df['mmsi_present'].sum() - geartype_vessels.sum()
    geartype_vessels['Other'] = other
  elif country.upper() in flag_list:
    geartype_vessels = df[df['flag'] == country.upper()].groupby('geartype')['mmsi_present'].sum().sort_values(ascending=False).head(5)
    other = df[df['flag'] == country.upper()]['mmsi_present'].sum() - geartype_vessels.sum()
    geartype_vessels['Other'] = other
  else:
    print('Invalid Country')
    return
  print(geartype_vessels)
  plt.figure(figsize=(8,4))
  plt.pie(geartype_vessels,labels=geartype_vessels.index,autopct='%1.1f%%',colors=sns.color_palette('deep'))
  plt.title(f"Distibution of {country.upper()} Vessels by Geartype ")

geartype_dis('ind')

# import plotly.express as px

# def density_df(country,gtype,activity,month):
#   if country.lower() == 'all':
#     print("Data is too big to process. Please choose one country at a time :)")
#   elif country.upper() in flag_list:
#     if gtype.lower() == 'all':
#       if activity.lower() == 'all':
#         if month == 'all':
#           df_temp = df[df['flag'] == country.upper()]
#         else:
#           df_temp = df[(df['flag'] == country.upper())&(df['month']==month)]
#         return df_temp
#       elif activity.lower() == 'loitering':
#         if month == 'all':
#           df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 1)]
#         else:
#           df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 1)&(df['month']==month)]
#         return df_temp
#       elif activity.lower() == 'not loitering':
#         if month == 'all':
#           df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 0)]
#         else:
#           df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 0)&(df['month']==month)]
#         return df_temp
#       else:
#         print('Invalid Activity')
#         return

#     elif gtype.lower() in gear_list:
#       if activity.lower() == 'all':
#         if month == 'all':
#           df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())]
#         else:
#           df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['month']==month)]
#         return df_temp
#       elif activity.lower() == 'loitering':
#         if month == 'all':
#           df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 1)]
#         else:
#           df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 1)&(df['month']==month)]
#         return df_temp
#       elif activity.lower() == 'not loitering':
#         if month == 'all':
#           df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 0)]
#         else:
#           df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 0)&(df['month']==month)]

#         return
#       else:
#         print('Invalid Activity')
#         return
#   else:
#     print('Invalid Country or Geartype')
#     return

# def visualize_density(df):
#   fig = px.density_map(df,lat='lat',lon='lon',z='mmsi_present',radius=10,zoom=1,title='Vessel Density Map')
#   fig.show()

# visualize_density('chn','all','all','all')

# def visualize_points(country,gtype,activity):
#   if country.lower() == 'all':
#     print("Data is too big to process. Please choose one country at a time :)")
#   elif country.upper() in flag_list:
#     if gtype.lower() == 'all':
#       if activity.lower() == 'all':
#         df_temp = df[df['flag'] == country.upper()]
#         fig = px.scatter_geo(df_temp,lat='cell_ll_lat',lon='cell_ll_lon',color='loitering',hover_name='mmsi_present',hover_data=["flag","geartype","loitering"],projection='orthographic')
#         fig.show()
#         return
#       elif activity.lower() == 'loitering':
#         df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 1)]
#         fig = px.scatter_geo(df_temp,lat='cell_ll_lat',lon='cell_ll_lon',color='loitering',hover_name='mmsi_present',hover_data=["flag","geartype","loitering"],projection='natural earth')
#         fig.show()
#         return
#       elif activity.lower() == 'not loitering':
#         df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 0)]
#         fig = px.scatter_geo(df_temp,lat='cell_ll_lat',lon='cell_ll_lon',color='loitering',hover_name='mmsi_present',hover_data=["flag","geartype","loitering"],projection='natural earth')
#         fig.show()
#         return
#       else:
#         print('Invalid Activity')
#         return

#     elif gtype.lower() in gear_list:
#       if activity.lower() == 'all':
#         df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())]
#         fig = px.scatter_geo(df_temp,lat='cell_ll_lat',lon='cell_ll_lon',color='loitering',hover_name='mmsi_present',hover_data=["flag","geartype","loitering"],projection='natural earth')
#         fig.show()
#         return
#       elif activity.lower() == 'loitering':
#         df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 1)]
#         fig = px.scatter_geo(df_temp,lat='cell_ll_lat',lon='cell_ll_lon',color='loitering',hover_name='mmsi_present',hover_data=["flag","geartype","loitering"],projection='natural earth')
#         fig.show()
#         return
#       elif activity.lower() == 'not loitering':
#         df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 0)]
#         fig = px.scatter_geo(df_temp,lat='cell_ll_lat',lon='cell_ll_lon',color='loitering',hover_name='mmsi_present',hover_data=["flag","geartype","loitering"],projection='natural earth')
#         fig.show()
#         return
#       else:
#         print('Invalid Activity')
#         return
#   else:
#     print('Invalid Country or Geartype')
#     return

# visualize_points('ind','trawlers','all')

# data_1 = density_df('usa','all','all','all')


# import pydeck as pdk

# COUNTRIES = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_scale_rank.geojson"

# view_state = pdk.ViewState(latitude=0, longitude=0, zoom=0, min_zoom=-5,max_zoom=15,pitch=0,
#     bearing=0,)

# # Set height and width variables
# view = pdk.View(type="_GlobeView", controller=True)


# layers = [
#     pdk.Layer(
#         "GeoJsonLayer",
#         id="base-map",
#         data=COUNTRIES,
#         stroked=False,
#         filled=True,
#         get_fill_color=[200, 200, 200],
#     ),
#     pdk.Layer(
#         "ColumnLayer",
#         id="power-plant",
#         data=data_1,
#         get_elevation="mmsi_present",
#         get_position=["lon", "lat"],
#         elevation_scale=1000,
#         pickable=True,
#         auto_highlight=True,
#         radius=20000,
#         get_fill_color=[160, 32, 240]
#     ),
# ]

# deck = pdk.Deck(
#     views=[view],
#     initial_view_state=view_state,
#     width = "100%",
#     height = 700,
#     tooltip={"text": "{flag}, {geartype}"},
#     layers=layers,
#     map_provider=None,
#     # Note that this must be set for the globe to be opaque
#     parameters={"cull": True},
# )

# deck.to_html("globe_view.html", css_background_color="black")

