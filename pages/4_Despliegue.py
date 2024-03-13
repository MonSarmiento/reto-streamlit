import streamlit as st
import pandas as pd
import numpy as np

#ST.DATAFRAME
def run():
  dataframe = np.random.randn(10, 20)
  st.dataframe(dataframe)
if __name__ == "__main__":
    run()

#PANDAS STYLER
import streamlit as st
import pandas as pd
import numpy as np
def run():
  dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
  st.dataframe(dataframe.style.highlight_max(axis=0))
if __name__ == "__main__":
    run()

#ST.TABLE
def run():
  dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
  st.table(dataframe)
if __name__ == "__main__":
    run()
