import streamlit as st
from PIL import Image
def run():


  image = Image.open('oso_panda.jpg')
  st.image(image, caption='Oso panda en la montaña')
if __name__ == "__main__":
  run()
#st.header('st.dataframe')
