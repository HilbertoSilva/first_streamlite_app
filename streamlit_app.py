import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('๐ฅฃ Omega 3 & Blueberry Oatmeal')
streamlit.text('๐ฅKale, Spinach & Rocket Smoothie')
streamlit.text('๐๐Hard-Boiled Free-Range Egg')
streamlit.text('๐ฅ๐Avocado Toast')

streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')

import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


streamlit.dataframe(my_fruit_list)


