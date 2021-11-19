import streamlit as st
import pandas as pd
import numpy as np
import datetime
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import requests



'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# map
st.sidebar.markdown('''
            # Pickoff adress
            ''')
street = st.sidebar.text_input("Street", "75 Bay Street")
city = st.sidebar.text_input("City", "Toronto")
province = st.sidebar.text_input("Province", "Ontario")
country = st.sidebar.text_input("Country", "Canada")

st.sidebar.markdown('''
            # Dropoff adress
            ''')
street2 = st.sidebar.text_input("Street", "74 Bay Street")
city2 = st.sidebar.text_input("City", "New York")
province2 = st.sidebar.text_input("Province", "New York")
country2 = st.sidebar.text_input("Country", "United-States")


geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+province+", "+country)
location2 = geolocator.geocode(street2+", "+city2+", "+province2+", "+country2)

lat = location.latitude
lon = location.longitude
lat2 = location2.latitude
lon2 = location2.longitude

map_data = pd.DataFrame({'lat': [lat2, lat], 'lon': [lon2, lon]})

st.map(map_data)
lat
lon
lat2
lon2

st.sidebar.markdown('''
            # Passenger count
            ''')


nbpassager = st.sidebar.slider('Select a number', 1, 6, 1)

nbpassager





# Ask Datetime to user
today = datetime.date.today()
start_date = st.date_input('Date', today)
time = st.time_input('Time', datetime.time(8, 00))

year = str(start_date.year)
hour = time.hour
minute = time.minute
hour
minute
start_date = str(start_date)


st.markdown('''
            # Price Prediction
            ''')

url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={start_date}%{year}:{hour}:{minute}&pickup_longitude={lon}&pickup_latitude={lat}&dropoff_longitude={lon2}&dropoff_latitude={lat2}&passenger_count={nbpassager}'

x = requests.get(url).json()
x["prediction"]

'''
1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''