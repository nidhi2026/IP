import streamlit as st
import streamlit.components.v1 as components
import requests
import webbrowser as web

def fetch_ip_address(url, ip_type):
    ip_script = f"""
    <style>
        .styled-button {{
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            margin-left: 10px;
        }}
        .styled-button:hover {{
            background-color: rgba(255, 255, 255, 0.3);
        }}
    </style>
    <script>
        fetch('{url}')
        .then(response => response.json())
        .then(data => {{
            document.getElementById("ip_display").innerText = data.ip;
        }})
        .catch(err => {{
            console.error("Error fetching IP:", err);
            document.getElementById("ip_display").innerText = "Failed to fetch IP.";
        }});
    </script>
    <div style="border:none; width:300px; display:flex; align-items:center; height: 20px;">
        <p style="font-size:20px; color:#FFFFFF; margin-right:10px;">{ip_type}: </p>
        <p id="ip_display" style="font-size:20px; color:#32ca5b;">Fetching IP...</p>
        <button class="styled-button" id="styled-button" onclick="copyIP()">Copy</button>
    </div>
    <script>
        function copyIP() {{
            document.getElementById("styled-button").innerText = 'Copied';
            let ip = document.getElementById("ip_display").innerText;
            navigator.clipboard.writeText(ip);
            setTimeout(() => {{
                document.getElementById("styled-button").innerText = 'Copy';
            }}, 1000);
        }}
    </script>
    """
    return ip_script


st.title("Your Public IP Address")

ipv4 = fetch_ip_address('https://api.ipify.org?format=json', 'IPV4')
components.html(ipv4, height=40)

ipv6 = fetch_ip_address('https://api64.ipify.org?format=json', 'IPV6')
components.html(ipv6, height=40)


st.markdown('---')

st.title("Get Location")

def get_geolocation(ip):
    geo_url = f'https://get.geojs.io/v1/ip/geo/{ip}.json'
    geo_q = requests.get(geo_url)
    if geo_q.status_code == 200:
        geo_d = geo_q.json()
        return geo_d
    else:
        st.error('Invalid IP address')


def fetch_ip_address():
    ip_script = f"""
    <style>
        .styled-button {{
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            margin-left: 10px;
        }}
        .styled-button:hover {{
            background-color: rgba(255, 255, 255, 0.3);
        }}
    </style>
    <script>
        fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {{
            document.getElementById("ip_display").innerText = data.ip;
        }})
        .catch(err => {{
            console.error("Error fetching IP:", err);
            document.getElementById("ip_display").innerText = "Failed to fetch IP.";
        }});
    </script>
    <div style="border:none; width:300px; display:flex; align-items:center; height: 20px;" >
        <p style="font-size:19px; color:#FFFFFF; margin-right:5px;">My IP:</p>
        <p id="ip_display" style="font-size:19px; color:#32ca5b;">Fetching IP...</p>
        <button class="styled-button" id="styled-button" onclick="copyIP()">Copy</button>
    </div>
    <script>
        function copyIP() {{
            document.getElementById("styled-button").innerText = 'Copied';
            let ip = document.getElementById("ip_display").innerText;
            navigator.clipboard.writeText(ip);
            setTimeout(() => {{
                document.getElementById("styled-button").innerText = 'Copy';
            }}, 1000);
        }}
    </script>
    """
    return ip_script


def format(data):
    return f'<span style="font-size:20px; color:#32ca5b;">{data}</span>'

components.html(fetch_ip_address(), height=40)

ip_address = st.text_input("Enter IP address:", placeholder='Enter IP...')

if ip_address:
    geo = get_geolocation(ip_address)
    if geo:
        st.markdown(f"""The IP address {format(geo['ip'])} is located in {format(geo['city'])}, 
                    {format(geo['region'])}, {format(geo['country'])}, with coordinates at latitude 
                    {format(geo['latitude'])} and longitude {format(geo['longitude'])}.
                The associated timezone is {format(geo['timezone'])}.
                 """, unsafe_allow_html=True)

        if st.button("Show Location"):
            maps_url = f"https://www.google.com/maps/@?api=1&map_action=map&center={geo['latitude']},{geo['longitude']}"
            try:
                web.open(maps_url)
            except:
                st.error("Website is not opening!!", icon="🚨")
