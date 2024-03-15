#RADIO BOTTOMS
def run():
  titanic_data=('pages/titanic.csv')
  selected_class = st.radio("Select Class", titanic_data['class'].unique())
  st.write("Select Class:",selected_class)
if __name__ == "__main__":
  run()
