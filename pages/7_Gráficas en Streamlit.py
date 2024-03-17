import altair as alt
import pandas as pd
import streamlit as st

#ALTAIR

movies_link = 'https://raw.githubusercontent.com/vega/vega/main/docs/data/movies.json'
movie_df = pd.read_json(movies_link)

#Con la siguiente instrucción, podrás ver que movie_df es en realidad un dataframe de Pandas que tiene 3201 películas (filas) con 16 características de información (columnas) cada una
movie_df.shape

#ejecutando la siguiente  instrucción se podrán visualizar las primeras 5 filas del dataframe
movie_df.head(5)
