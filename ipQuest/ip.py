import streamlit as st
import requests

st.title("Find Your IP Address using ipframe")
st.markdown("""
    <iframe src="https://api64.ipify.org?format=jsonp&callback=mycallback" 
            style="border:none; height:50px; width:300px;"></iframe>
""", unsafe_allow_html=True)

st.markdown("---")

st.title("Find Your IP Address using ipify")
ip_address = requests.get('https://api.ipify.org?format=json').json()
ipv6 = requests.get('https://api64.ipify.org?format=json').json()
st.write(f"Your IP Address is: {ip_address['ip']}")
st.write(f"Your IP Address is: {ipv6['ip']}")

st.markdown("---")

st.title("Find Your IP Address using js")
ip_fetcher = """
    <script>
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ip_address').innerText = "Your IP Address is: " + data.ip;
        })
        .catch(error => {
            console.error('Error fetching IP address:', error);
        });
    </script>
    <div id="ip_address">Fetching your IP address...</div>
"""
st.markdown(ip_fetcher, unsafe_allow_html=True)
