#IMAGEN JPG
import streamlit as st
from PIL import Image

def run():
  st.header('st.image')
  image = Image.open('/mount/src/reto-streamlit/pages/oso_panda.jpg')
  st.image(image, caption='Oso panda en la montaña')
  #funcion para animacion
if __name__ == "__main__":
  run()

#AUDIO
audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')
