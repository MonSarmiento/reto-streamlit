import streamlit as st
pip install vega_datasets
#ALTAIR
from vega_datasets import data as vega_data
import pandas as pd
movie_df = pd.read_json(vega_data.movies.url)


