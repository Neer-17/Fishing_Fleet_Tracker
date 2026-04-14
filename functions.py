import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Datasets/combined_dataset.csv')

plt.style.use('dark_background')

#Count of Origins of the ships
flag_list = df['flag'].unique()
flag_list = flag_list.tolist()
flag_list2 = flag_list.copy()
flag_list.insert(0,'ALL')
countries = [country for country in flag_list if len(country)==3]
unknown = [country for country in flag_list if len(country)!=3]


#Types of gears used for fishing
gear_list = df['geartype'].unique()
gear_list = gear_list.tolist()
gear_list.insert(0,'All')


#Distribution of Vessels by Country
def country_dis():
  most_vessels_by_countries = df.groupby('flag')['mmsi_present'].sum().sort_values(ascending=False).head(19)
  other = df['mmsi_present'].sum() - most_vessels_by_countries.sum()
  most_vessels_by_countries['Other{279 Flags}'] = other
  return most_vessels_by_countries

# Distribution of Vessels by Activity
def activity_dis(country):
  if country.lower() == 'all':
    loitering_vessels = df.groupby('loitering')['mmsi_present'].sum()
  elif country.upper() in flag_list:
    loitering_vessels = df[df['flag'] == country.upper()].groupby('loitering')['mmsi_present'].sum()
  else:
    print('Invalid Country')
  return loitering_vessels


# Distribution of Vessels by Geartype
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
  return geartype_vessels
  
# Function to get Data
def get_data(country,gtype,activity,month):
  print('In the function')
  if country.lower() == 'all':
    return "Data is too big to process. Please choose one country at a time :)"
  elif country.upper() in flag_list:
    if gtype == 'All':
      if activity.lower() == 'both':
        if month == 'all':
          df_temp = df[df['flag'] == country.upper()]
        else:
          df_temp = df[(df['flag'] == country.upper())&(df['month']==month)]
        return df_temp
      elif activity.lower() == 'loitering':
        if month == 'all':
          df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 1)]
        else:
          df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 1)&(df['month']==month)]
        return df_temp
      elif activity.lower() == 'non loitering':
        if month == 'all':
          df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 0)]
        else:
          df_temp = df[(df['flag'] == country.upper()) & (df['loitering'] == 0)&(df['month']==month)]
        return df_temp
    elif gtype in gear_list:
      if activity.lower() == 'both':
        if month == 'all':
          df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())]
        else:
          df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['month']==month)]
        return df_temp
      elif activity.lower() == 'loitering':
        if month == 'all':
          df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 1)]
        else:
          df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 1)&(df['month']==month)]
        return df_temp
      elif activity.lower() == 'non loitering':
        if month == 'all':
          df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 0)]
        else:
          df_temp = df[(df['flag']==country.upper())&(df['geartype'] == gtype.lower())&(df['loitering'] == 0)&(df['month']==month)]
        return df_temp
      else:
        print('Invalid Activity')
        return

# Function to plot Vessels on Globe
def globe_plot(data):
  COUNTRIES = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_scale_rank.geojson"

  view_state = pdk.ViewState(latitude=0, longitude=0, zoom=0, min_zoom=-5,max_zoom=15,pitch=0,
      bearing=0,)

  # Set height and width variables
  view = pdk.View(type="_GlobeView", controller=True)


  layers = [
      pdk.Layer(
          "GeoJsonLayer",
          id="base-map",
          data=COUNTRIES,
          stroked=False,
          filled=True,
          get_fill_color=[200, 200, 200],
      ),
      pdk.Layer(
          "ColumnLayer",
          id="power-plant",
          data=data,
          get_elevation="mmsi_present",
          get_position=["lon", "lat"],
          elevation_scale=1000,
          pickable=True,
          auto_highlight=True,
          radius=20000,
          get_fill_color=[36, 255, 248]
      ),
  ]

  deck = pdk.Deck(
      views=[view],
      initial_view_state=view_state,
      width = "100%",
      height = 700,
      tooltip={"text": "{flag}, {geartype}"},
      layers=layers,
      map_provider=None,
      # Note that this must be set for the globe to be opaque
      parameters={"cull": True},
  )

  return deck

