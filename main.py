
from re import T
from importlib_metadata import distribution
import streamlit as st 
import plotly.express as px
import pandas as pd
import seaborn as sns
header=st.container()
dataset=st.container()
features=st.container()
with header:
     st.title("welcome to my awesome project")
     st.text('In this project we look into the rise of global temperatures over the years.In present day the world is experiencing enornomous effects of climate change including:droghts, tsunamis and extinction of animal and tree species.These are all as a result of rise in global temperatures')
with dataset:
     st.header('Global land temperatures')  
     st.text('This data has been extracted from United Nations Statistics Division-UNSD website')   
     temperature_data =pd.read_csv('C:/Users/EDWIN/Desktop/data/temperature.csv')
     st.write(temperature_data.head())
     st.header('Temperature distribution')
     temperatur_dist=pd.DataFrame(temperature_data["AverageTemperatureFahr"].value_counts()).head(20)
     st.bar_chart(temperatur_dist)
     sns.lineplot(data=temperature_data, x="year", y="AverageTemperatureFahr")
     line_chart_data=temperature_data.copy()
     #temperature_cross_tab=pd.crosstab(line_chart_data['year'],line_chart_data['AverageTemperatureFahr'])

      #Add sidebar and sidebar settings settings
     st.sidebar.subheader('Visualization settings')
    
     
uploaded_file=st.sidebar.file_uploader(label="upload your csv or Excel file.",
type=['csv','xlsx'])
if uploaded_file is not None:
    print('hello')
chart_select=st.sidebar._selectbox(
    label='select the chart type',
    options=['scatter plots','lineplots','Histogram','Boxplots','bar_chart']
)
   #Barchart
st.header('Temperature Vs Year')
df=temperature_data.copy()
fig=px.bar(df,x='year',y='AverageTemperatureFahr')
st.write(fig)
     
