#RADIO BOTTOMS
import pandas as pd
import streamlit as st

def run():
  titanic_data=pd.read_csv('pages/titanic.csv')
  selected_class = st.radio("Select Class", titanic_data['class'].unique())
  st.write("Select Class:",selected_class)
if __name__ == "__main__":
  run()
