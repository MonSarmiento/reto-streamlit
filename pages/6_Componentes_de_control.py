#RADIO BOTTOMS
import pandas as pd
import streamlit as st

#def run():
titanic_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/titanic.csv'
titanic_data = pd.read_csv(titanic_link)
selected_class = st.radio("Select Class", titanic_data['Pclass'].unique())
st.write("Select Class:",selected_class)
#if __name__ == "__main__":
  #run()

#selected_class = sidebar.radio("Select Class", titanic_data['class'].unique())

#st.write("Selected Class:", selected_class)
#st.success(f'Selected Class: {selected_class}') 
