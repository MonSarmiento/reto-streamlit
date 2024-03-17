import altair as alt


#ALTAIR
titanic_link = 'https://raw.githubusercontent.com/MonSarmiento/reto-streamlit/main/pages/titanic.csv'
titanic_data = pd.read_csv(titanic_link)

alt.Chart(titanic_data).mark_point()

