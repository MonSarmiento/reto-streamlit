#RADIO BOTTOMS
def run():
  selected_class = st.radio("Select Class", titanic_data['class'].unique())
  st.write("Select Class:",selected_class)
