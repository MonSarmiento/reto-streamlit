import streamlit as st
import pandas as pd
import numpy as np
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)

def run():
  dataframe = np.random.randn(10, 20)
  st.dataframe(dataframe)
  
