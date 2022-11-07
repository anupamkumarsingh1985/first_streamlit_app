import streamlit

streamlit.title("🥣 My First Streamlit Project");

streamlit.header("Breakfast Menu");

streamlit.text("Egg and Omlette");

streamlit.text("Poha and Misal Pav");


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");

my_fruit_list = my_fruit_list.set_index('Fruit');

fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Strawberries']);

fruit_to_show = fruit_to_show.loc[fruit_selected];

streamlit.dataframe(fruit_to_show);
