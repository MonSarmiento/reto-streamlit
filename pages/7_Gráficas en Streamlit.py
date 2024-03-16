#import streamlit as st
from altair.utils.deprecation import deprecated
#ALTAIR
from vega_datasets import datasets as vega_data
import pandas as pd
movie_df = pd.read_json(vega_data.movies.url)


