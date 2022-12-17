import streamlit as st
import pandas as pd
import numpy as np

#name = input("Enter your name: ")

st.title(f"Basic Streamlit application")

# Header

st.header("This is a demonstration.")

# subheader

st.subheader(f"Warm welcome.")

# Markdowns

st.markdown("""---""")

st.markdown("# This is markdown header-1")
st.markdown("## This is markdown header-2")
st.markdown("### This is markdown header-3")

st.markdown("""---""")

st.markdown("$$ a^2+ b^2 = c^2 $$")

# Simple text writing

st.text("This is a simple text")

# Write method
st.write("This is written using write function.")

st.write(range(10))

data = np.random.randn(10,2)
df = pd.DataFrame(data, columns=['A', 'B'])

st.write(df)

st.markdown("""---""")

# Display images

from PIL import Image
img = Image.open("lm10.jpeg")

col1, col2 = st.columns([6,4])

with col1:
    st.image(img, width=400)

with col2:
    st.write("Hi I am Lionel Messi. You know who I am !!!")

st.markdown("- I play for Argentina.")
st.markdown("- I also play for PSG.")
st.markdown("- I scored 5 goals in FIFA WC-2022 Qatar.")