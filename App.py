# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:25:13 2025

@author: Thato 
"""

import streamlit as st

st.write("Hello, Streamlit!")

st.title("Seto State System")
st.write("Industrial Revolution Thinking")

st.title("this is my first web page")

number = st.slider("pick a number", 1, 100)

st.write(f"You picked: {number}")
         
# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)         

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Mr. Thato Tshepang Sekgoele"
field = "Data Science"
institution = "University of Johanneburg"

st.write("The Fourth Industrial Revolution Thinking has \n"
         "enabled a transdisciplinary approach, to push the envelope of creativity through:\n"
         "Computational thinking, Engineering thinking, Mathematical thinking, Quantum thinking , and the Art and Science of thinking.\n"
         "Such thinking, through knowledge mutation is to push the envelope of design of high-performance systems and energy-efficient computing power.")
st.write("By design of high-performance systems, our national grid through NICIS, NITHeCS, SKA, NERSA and NECSA we shall harmonise intelligest systems to effectively and efficiently improve computing speed and infrastructure network. The drivers of Artificial Intelligence and Computational Intelligence methords, are reengineering conventional systems and constructing robust smart grid systems that are self-organising. ")

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "thato.malaisha@gamil.com"
st.write(f"You can reach {name} at {email}.")
st.write("")