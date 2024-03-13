from PIL import Image
def run():
  st.header('st.dataframe')
  image = Image.open('https://github.com/MonSarmiento/reto-streamlit/blob/main/oso_panda.jpg')
  st.image(image, caption='Oso panda en la montaña')
  if __name__ == "__main__":
    run()
