#RADIO BOTTOMS
import pandas as pd
import streamlit as st

titanic_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/titanic.csv'
titanic_data = pd.read_csv(titanic_link)
selected_class = st.radio("Select Class", titanic_data['Pclass'].unique())
st.write("Select Class:",selected_class)

# SELECT BOX
selected_sex = st.selectbox("Select Sex", titanic_data['Sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")
