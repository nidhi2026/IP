import streamlit as st

def ip():
    st.title("Find Your IP Address")

    # Embed an iframe to display the user's IP using ipify's widget
    st.markdown("""
        <iframe src="https://api64.ipify.org?format=jsonp&callback=mycallback" 
                style="border:none; height:50px; width:300px;"></iframe>
    """, unsafe_allow_html=True)
