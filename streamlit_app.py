import pandas
import streamlit
import requests
import snowflake.connector

streamlit.title('Hello,World')
streamlit.header('🥣 🥗 Breakfast Menu  🥑🍞')
streamlit.text('🥣 🥗Omega and blueberry oatmeal')
streamlit.text('🥑spinach and avacado smoothie')
streamlit.text('🐔boiled eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#streamlit.dataframe(my_fruit_list)

# we can select any fruit here from pickup list
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


# We will get only Avocado and strawberries here
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice API response time 
fruityice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityice_response)


#New Section to display fruityvice API response
streamlit.header('FruityVice Fruit Advice')
fruityice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityice_response.json())


Fruityvice_normalized = pandas.json_normalize(fruityice_response.json())
streamlit.dataframe(Fruityvice_normalized)



fruit_choice=streamlit.text_input('what fruit would you like information about?')
streamlit.write('User enter',fruit_choice)
fruityice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


#snowflake-connector-python
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
