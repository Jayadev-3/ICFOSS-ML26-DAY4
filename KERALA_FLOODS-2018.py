from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Kerala Floods 2018")
st.header(
    "Data on warning, fatalities, camps, rainfall during the flood occurred in 2018")
st.text("Context:During August 2018, severe floods affected the south Indian state Kerala,"
        "due to unusually high rainfall during the monsoon season. It was the worst flood in Kerala in "
        "nearly a century. Over 483 people died, and 140 are missing. About a million people were evacuated."
        "All 14 districts of the state were placed on red alert. According to the Kerala government, one-sixth "
        "of the total population of Kerala had been directly affected by the floods and related incidents."
        "The Indian government had declared it a Level 3 Calamity, or calamity of a severe nature.")

img = Image.open("pic.jpg")
st.image(img, width=700, caption='Kerala Floods 2018')

st.subheader("The dataset contains some data about 2018 Kerala flood casualties, warnings, district wise warnings, and rainfall.")
df = pd.read_csv('district_wise_details.csv')
df

st.subheader("BARPLOT - Fatalities - number of people died")
sns.barplot(x='fatalities', y='district', data=df)
st.pyplot()

st.subheader("Normal Rainfall Vs Actual Rainfall")
img = Image.open("rain.jpg")
st.image(img, width=700, caption='Rainfall')
plt.plot(df.normal_rainfall_in_mm, df.district)
plt.plot(df.actual_rainfall_in_mm, df.district)
plt.xlabel("Rainfall in 'mm'")
st.pyplot()

st.subheader("Difference in Rainfall(Actual-Normal)")
diff = np.array(df.actual_rainfall_in_mm - df.normal_rainfall_in_mm)
plt.plot(diff, df.district)
st.pyplot()

st.subheader("JOINTPLOT - LANDSLIDES")
img = Image.open("land.jpg")
st.image(img, width=700, caption='Landslides')
sns.jointplot(x='no_of_landslides', y='district', data=df)
st.pyplot()

st.subheader("Acknowledgements")
st.text("Data is taken from the additional memorandum, Kerala Floods – 2018 by State Relief Commissioner, Disaster Management. The complete report can be found here: https://sdma.kerala.gov.in/wp-content/uploads/2019/08/Memorandum2-Floods-2018.pdf")
st.text("https://www.kaggle.com/imdevskp/kerala-floods-2018")

st.subheader("PREPARED BY : JAYADEV P U")
st.text("ICFOSS-ML26-DAY4-ASSIGNMENT")
