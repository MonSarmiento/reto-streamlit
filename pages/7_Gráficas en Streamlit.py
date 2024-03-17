!pip install altair
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

#ALTAIR

movies_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/movies.csv'
movie_df = pd.read_csv(movies_link)

#Con la siguiente instrucción, podrás ver que movie_df es en realidad un dataframe de Pandas que tiene 3201 películas (filas) con 16 características de información (columnas) cada una
movie_df.shape

#ejecutando la siguiente  instrucción se podrán visualizar las primeras 5 filas del dataframe
movie_df.head()

#columnas del dataframe
movie_df.columns

#se usará la función to_datetime dentro de Pandas para convertir la columna Release_Date en una fecha real y luego extraer el valor del 'año'
def extract_year(value):
       return pd.to_datetime(value, format='%b %d %Y').year

movie_df['Year'] = movie_df["Release Date"].apply(extract_year)
movie_df

#dataframe de peliculas del 2000
movie_2000 = movie_df[movie_df["Year"] == 2000]
movie_2000

#grafica de relacion
alt.Chart(movie_2000).mark_point().encode(
     alt.X('Production Budget'),
     alt.Y('Worldwide Gross')
)

import altair as alt

# load a simple dataset as a pandas DataFrame

alt.Chart(movie_2000).mark_point().encode(
    x='Production Budget',
    y='Worldwide Gross',
    color='Origin',
)
