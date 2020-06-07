import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = (
"C:/Users/w1n5t/Desktop/coding/stkorea/motor_collision_korea.csv"
)

st.title("Motor Vehicle Collisions in Korea")
st.markdown("This streamlit application is using for "
"monitoring motor vehicle Collisions in Korea domestically")

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows,encoding='CP949')
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace = True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis= 'columns', inplace= True)
    data.rename(columns = {'crash_year' : 'year'})
    return data


data = load_data(10000)

st.header("where are the most people injured in korea?")
injured_people = st.slider("Number of persons who injured by Motor collision", 0, 23)
st.map(data.query("injured_persons > @injured_people")[["latitude", "longitude"]].dropna(how = "any"))


if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)
