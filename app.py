import streamlit as st
import os 




# Set the page configuration
st.set_page_config(page_title="Design Guidelines", layout="wide")

# Add a header with a brief introduction to the design guidelines
st.markdown("# 4ever* Design Guidelines")
st.markdown("This page provides a guide to the design elements, user experience and assets used in our frontend. Please refer to our designer for any questions or concerns regarding the visual identity of our application.")

# UIX diagram
with st.expander("User experience", expanded=True):
    st.image("assets/uix.svg")

# Icons
with st.expander("Logo's & icons "):
    # Directory containing SVG icons
    icon_directory = "icons"

    # List of SVG icons
    icons = ["icon_app_dark.svg", "icon_app_light.svg", "icon_app_outline.svg", "logo_dark.svg", "logo_light.svg", "logo_with-icon_dark.svg", "logo_with-icon_light.svg"]  # Add your icon file names here

    # Calculate the number of columns you want in each row
    num_columns = 3
    rows = [icons[i:i + num_columns] for i in range(0, len(icons), num_columns)]

    # Display SVG icons in a grid using Streamlit columns
    for row in rows:
        cols = st.columns(num_columns)
        for col, icon in zip(cols, row):
            with col:
                with open(os.path.join(icon_directory, icon), "r") as svg_file:
                    svg_content = svg_file.read()
                    st.markdown(f'<div style="width: 100%; height: auto; margin-bottom: 40px;">{svg_content}</div>', unsafe_allow_html=True)
                st.caption(icon)

    # Add download link for icons and images
    with open("assets/logos.zip", "rb") as file:
        btn = st.download_button(
            label="Download all assets",
            data=file,
            file_name="logos.zip",
            mime="application/zip"
        )

# Color Palette
with st.expander("Colors"):
    st.markdown("""
        <span style='color:  #9A7B69'>Primary:</span>   #9A7B69 (Bronze)<br>
        <span style='color:  #1a1919'>Secondary:</span>   #1a1919  (Black)<br>
        <span style='color:  #efedea'>Accent:</span>   #efedea (Beige)<br>
        <span style='color:  #f6f4f2ff'>Background:</span>   #f9f9f9  (Light-beige)
        """, unsafe_allow_html=True)

# Typography
with st.expander("Typography"):
    st.markdown("""
        We use ```font-family: Open Sans```<br><br>
        <span style='font-family: Open Sans; font-size: 24px'>These are the sizes for the headers:</span><br> 24px, 18px, 14px<br><br>
        <span style='font-family: Open Sans; font-size: 16px'>These are the sizes for the body:</span><br> 16px <br>
        """, unsafe_allow_html=True)

