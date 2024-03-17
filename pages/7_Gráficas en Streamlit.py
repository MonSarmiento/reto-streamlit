import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

#ALTAIR
st.write("ALTAIR")
movies_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/movies.csv'
movie_df = pd.read_csv(movies_link)

#Con la siguiente instrucción, podrás ver que movie_df es en realidad un dataframe de Pandas que tiene 3201 películas (filas) con 16 características de información (columnas) cada una
movie_df.shape

#ejecutando la siguiente  instrucción se podrán visualizar las primeras 5 filas del dataframe
movie_df.head()

#columnas del dataframe
movie_df.columns

#se usará la función to_datetime dentro de Pandas para convertir la columna Release_Date en una fecha real y luego extraer el valor del 'año'
def extract_year(value):
       return pd.to_datetime(value, format='%b %d %Y').year

movie_df['Year'] = movie_df["Release Date"].apply(extract_year)
movie_df

#dataframe de peliculas del 2000
movie_2000 = movie_df[movie_df["Year"] == 2000]
movie_2000

#grafica de relacion
alt.Chart(movie_2000).mark_point().encode(
     alt.X('Production Budget'),
     alt.Y('Worldwide Gross')
)

alt.Chart(movie_2000).mark_point(filled=True).encode(
    alt.X('Production Budget'),
    alt.Y('Worldwide Gross'),
    alt.Size('US Gross')
)

#opacidad
alt.Chart(movie_2000).mark_point(filled=True).encode(
    alt.X('Production Budget'),
    alt.Y('Worldwide Gross'),
    alt.Size('US Gross'),
    alt.Color('Major Genre'),
    alt.OpacityValue(0.7)
)

#Para poder movernos por el gráfico y ver los detalles de las película que están representadas en cada circulo se emplea la herramienta Tooltip
alt.Chart(movie_2000).mark_point(filled=True).encode(
    alt.X('Production Budget'),
    alt.Y('Worldwide Gross'),
    alt.Size('US Gross'),
    alt.Color('Major Genre'),
    alt.OpacityValue(0.7),
    tooltip = [alt.Tooltip('Title'),
               alt.Tooltip('Production Budget'),
               alt.Tooltip('Worldwide Gross'),
               alt.Tooltip('US Gross')
              ]
)

##BOKEH

st.write("BOKEH")
#mi_primer_grafico.py 
#from bokeh.plotting import figure, output_file, show
#output_file('my_first_graph.html')

#p = figure()
#p.circle(x, y, size=10, color='red', legend='circle')
#p.line(x, y, color='blue', legend='line')
#ptriangle(y, x, color='gold', size=10, legend='triangle')

#En el siguiente código se establece tamaño, color y nombre de leyenda para cada glifo
#p.legend.click_policy='hide'
#show(p)

#otro ejemplo para visualizar
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('columndatasource_example.html')

df=movie_2000
sample = df.sample(50)
source = ColumnDataSource(sample)
p = figure()
p.circle(x='Production Budget', y='Worldwide Gross',
         source=source,
         size=10, color='green')

##otro ejemplo
#column datasource.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('columndatasource_example.html')

movies_link = 'https://raw.githubusercontent.com/vega/vega/main/docs/data/movies.json'
df = pd.read_json(movies_link)

sample = df.sample(100)
source = ColumnDataSource(sample)

p = bokeh.plotting.figure(
    width=400,
    height=300,
    x_axis_label="Production Budget",
    y_axis_label="Worldwide Gross",
)
p.title.text = 'Movies'
p.circle(x='Production Budget', y='Worldwide Gross',
         source=source,
         size=10, color='orange')

hover = HoverTool() 
hover.tooltips=[
    ('Title', '@Title'), 
    ('Director', '@Director'), 
    ('Distributor', '@Distributor'),
    ('Production Budget', '@Production Budget')
]
p.add_tools(hover) 

bokeh.io.show(p)

from bokeh.plotting import figure, show

p = figure(width=400, height=400)
p.hbar(y=[1, 2, 3], height=0.5, left=0,
       right=[1.2, 2.5, 3.7], color="navy")

show(p)


###PLOTLY
st.write("PLOTLY")
import pandas as pd
import plotly.express as px

df =pd.read_csv("https://raw.githubusercontent.com/jeaggo/datasets/master/Superstore.csv")
fig = px.scatter(df, x="Order Date", y="Sales", color="Category",                   
                 size="Discount", hover_data=['Profit'])
fig.show()
