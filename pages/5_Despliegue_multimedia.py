#IMAGEN JPG
import streamlit as st
from PIL import Image

def run():
  st.header('st.image')
  image = Image.open('/mount/src/reto-streamlit/pages/oso_panda.jpg')
  st.image(image, caption='Oso panda en la montaña',width=300)
  #funcion para animacion
if __name__ == "__main__":
  run()

#2 IMAGENES
def run():
  st.header('2 IMAGENES')
  image1 = Image.open('/mount/src/reto-streamlit/pages/oso_panda.jpg')
  image2 = Image.open('/mount/src/reto-streamlit/pages/descarga.png')
  st.image([image1,image2], caption=['Oso panda en la montaña', 'equipo de trabajo'],width=300)
  #funcion para animacion
if __name__ == "__main__":
  run()

#AUDIO
def run():
  #audio_file = open('myaudio.ogg', 'rb')
  #audio_bytes = audio_file.read()
  st.audio('https://music.amazon.com.mx/albums/B00F99E7FG?marketplaceId=ART4WZ8MWBX2Y&musicTerritory=MX&ref=dm_sh_4MJTFyMCIDEUO044SAQgjzv6w&trackAsin=B00F99EAP8')
if __name__ == "__main__":
  run()


#VIDEO
def run():
  st.video('https://www.youtube.com/watch?v=Aq-oecPyPRA')
  st.caption('video tutorial')
if __name__ == "__main__":
  run()
