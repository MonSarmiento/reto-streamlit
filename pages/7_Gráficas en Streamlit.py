import streamlit as st

#ALTAIR
from vega_datasets import data as vega_data
import pandas as pd
movie_df = pd.read_json(vega_data.movies.url)


