
###PLOTLY
st.write("PLOTLY")
import pandas as pd
import plotly.express as px

df =pd.read_csv("https://raw.githubusercontent.com/jeaggo/datasets/master/Superstore.csv")
fig = px.scatter(df, x="Order Date", y="Sales", color="Category",                   
                 size="Discount", hover_data=['Profit'])
fig.show()
