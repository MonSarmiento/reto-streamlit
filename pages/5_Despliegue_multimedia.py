def run():
  from PIL import Image
  st.header('st.dataframe')
  image = Image.open('oso_panda.jpg')
  st.image(image, caption='Oso panda en la montaña')
  if __name__ == "__main__":
    run()
