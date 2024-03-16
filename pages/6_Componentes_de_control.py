#RADIO BOTTOMS
import pandas as pd
import streamlit as st

titanic_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.header('RADIO BOTTOMS')
selected_class = st.radio("Select Class", titanic_data['Pclass'].unique())
st.write("Select Class:",selected_class)

# SELECT BOX
st.header('SELECT BOX')
selected_sex = st.selectbox("Select Sex", titanic_data['Sex'].unique())
#st.write para desplegar la casilla de verificación
# la letra “f”, lo cual indica que se capturará información
# se pone el signo de admiración y la letra “r” para indicar que se escribirá la opción que se haya elegido.
st.write(f"Selected Option: {selected_sex!r}")

#SLIDERS
st.header('SLIDER')
# Creamos sidebar
#sidebar = st.sidebar
# variable que contendrá el expansor
optionals = st.expander("Optional Configurations", True)
#variable que contendrá el valor seleccionado en el control deslizante
fare_select = optionals.slider( 
  "Select the Fare",
  min_value = float(titanic_data['Fare'].min()),
  max_value = float(titanic_data['Fare'].max())
)
# “subset_fare”: variable que contendrá el conjunto de datos máximos y mínimos de los datos que se utilizarán para generar los controles deslizantes
subset_fare = titanic_data[(titanic_data['Fare'] >= fare_select)]
#st.write ayuda a plasmar las barras deslizantes en la aplicación web. Se debe anteponer la letra “f” al título que aparecerá debajo del control deslizante.
st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")
st.dataframe(subset_fare)
