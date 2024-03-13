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

    st.write(data_frame)#: muestra el conjunto de datos como una tabla.
    st.write(error)#: imprime una excepción especialmente.
    st.write(func)#: muestra información sobre una función.
    st.write(module)#: muestra información sobre el módulo.
    st.write(dict)#: muestra el diccionario en un widget interactivo.
    st.write(mpl_fig)#: muestra una figura de la librería Matplotlib.
    st.write(altair)#: muestra un gráfico de la librería Altair.
    st.write(keras)#: muestra un modelo de Keras.
    st.write(graphviz)#: muestra un gráfico de la librería Graphviz.
    st.write(plotly_fig)#: muestra un gráfico de la librería Plotly.
    st.write(bokeh_fig)#: muestra un gráfico de la librería Bokeh.
    st.write(sympy_expr)#: despliega la expresión SymPy usando LaTeX.
    st.write(htmlable)#: despliega _repr_html_ () para el objeto si está disponible.
    st.write(obj)#: despliega una cadena objeto si se desconoce lo contrario.
if __name__ == "__main__":
    run()
