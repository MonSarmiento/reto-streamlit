import altair as alt
import pandas as pd
import streamlit as st

#ALTAIR

titanic_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/titanic.csv'
titanic_data = pd.read_csv(titanic_link)
df_edad = titanic_data[titanic_data["Age"] >= 30]
df_edad.shape
alt.Chart(df_edad).mark_point().encode(
  alt.X('Age'),
  alt.Y('Pclass')
)
