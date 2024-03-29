import streamlit as st
from streamlit.logger import get_logger
import pandas as pd

LOGGER = get_logger(__name__)

def run():
    #titulo pagina
    st.set_page_config(
        page_title="Reto final",
        page_icon="👋",
    )

    st.write("# Pagina de Mónica! 👋")
   
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """,
    )
    df = pd.DataFrame({'col1': [1,2,3]})
    df # <-- Despliega el conjunto de datos
    x = 10
    'x', x # <-- Escribe el carácter ‘x’ y luego el valor de x
    st.title('Este es el título')
    st.header('Este es un encabezado')
    st.subheader('Este es un subencabezado')
    st.text('Aqui va mi texto')
    st.markdown('Streamlit es **realmente cool**.')
    st.markdown('Hola, **_mundo_** :sunglasses')
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a          r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

if __name__ == "__main__":
    run()
