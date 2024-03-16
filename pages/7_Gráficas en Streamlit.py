#import streamlit as st
from altair.utils.deprecation import deprecated

@deprecated("load_dataset is deprecated. " "Use the vega_datasets package instead.")
def load_dataset(name):
    """Load a dataset by name as a pandas.DataFrame."""
    import vega_datasets

    return vega_datasets.data(name)


@deprecated("load_dataset is deprecated. " "Use the vega_datasets package instead.")
def list_datasets():
    """List the available datasets."""
    import vega_datasets

    return vega_datasets.data.list_datasets()
#ALTAIR
from vega_datasets import datasets as vega_data
import pandas as pd
movie_df = pd.read_json(vega_data.movies.url)


