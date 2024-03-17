import altair as alt


#ALTAIR
from vega_datasets import datas as vega_data
import pandas as pd
movie_df = pd.read_json(vega_data.movies.url)
movie_df.head(5)

