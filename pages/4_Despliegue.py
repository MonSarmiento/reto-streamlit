import streamlit as st
import pandas as pd
import numpy as np

#ST.DATAFRAME
def run():
  st.header('st.dataframe')
  dataframe = np.random.randn(10, 20)
  st.dataframe(dataframe)
if __name__ == "__main__":
    run()

#PANDAS STYLER
import streamlit as st
import pandas as pd
import numpy as np
def run():
  st.header('Pandas Styler')
  dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
  st.dataframe(dataframe.style.highlight_max(axis=0))
if __name__ == "__main__":
    run()

#ST.TABLE
def run():
  st.header('st.table')
  dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
  st.table(dataframe)
if __name__ == "__main__":
    run()
  
#WIDGET
import streamlit as st
def run():
  st.header('Widget:st.slider')
  x = st.slider('x') # 👈 este es un widget
  st.write(x, 'al cuadrado es', x * x)
if __name__ == "__main__":
    run()


import streamlit as st
def run():
  st.header('widgets a través de una clave')
  st.text_input("Your name", key="name")
  # You can access the value at any point with:
  st.header('Hola:')
  st.session_state.name
if __name__ == "__main__":
    run()  
