import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit PYWEEK")
st.header("Demonstrating")
st.subheader("Here's a sample dataframe:")
st.text("Below is a randomly generated dataframe using Pandas and NumPy.")
st.latex(r'''E = mc^2''')

name= st.text_input("Enter your name:", "Type here...")
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)
gender = st.radio("Select your gender:", ("Male", "Female"))
hobbies = st.multiselect("Select your hobbies:", ["Reading", "Traveling", "Gaming", "Cooking", "Sports"])
rate = st.slider("Rate your experience (1-10):", 1, 10, 5) 
date = st.date_input("Select a date:")
colors = st.color_picker("Pick a color:")  

if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Hobbies: {', '.join(hobbies)}")
    st.write(f"Favorite Color: {colors}")
    st.success("Form submitted successfully!")

data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 5, 6, 7]  # Added a fourth value to match length of A
})
st.write("Here's the data:")
st.dataframe(data)
st.table(data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['x', 'y', 'z'])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

st.sidebar.title("Sidebar Example")
choice = st.sidebar.selectbox("Choose an option:", ["Home", "Data", "About"])

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit Logo")
    camera_input = st.camera_input("Take a picture")
with col2:
    st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")

with col3:
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        st.success("All features demonstrated!")
        st.warning("This is a sample warning message.")
        st.error("This is a sample error message.")
        st.info("This is a sample info message.")

        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)


