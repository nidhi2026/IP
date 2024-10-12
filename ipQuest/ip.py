import streamlit as st
import requests

st.title("Find Your IP Address using ipframe")
st.markdown("""
    <iframe src="https://api64.ipify.org?format=jsonp&callback=mycallback" 
            style="border:none; height:50px; width:300px;"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.title("Find Your IP Address using ipify")
ip_address = requests.get('https://api64.ipify.org?format=json').json()
st.write(f"Your IP Address is: {ip_address['ip']}")
