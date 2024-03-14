#IMAGEN JPG
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
def run():
  st.header('st.image')
  image = Image.open('/mount/src/reto-streamlit/pages/oso_panda.jpg')
  st.image(image, caption='Oso panda en la montaña')
  #funcion para animacion
if __name__ == "__main__":
  run()
def load_lottieurl(url):
  r=requests.get(url)
  if r.status_code != 200 :
    return None
  return r.jason()
lottie_coding = load_lottieurl("https://lottie.host/075ab19b-23cd-45a8-9980-4f3004626673/1vnfbbKSQx.json")

#AUDIO
