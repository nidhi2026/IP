import streamlit as st
import streamlit.components.v1 as components
import requests

st.title("Find Your IP Address using iframe")
st.markdown("""
    <iframe src="https://api64.ipify.org?format=jsonp&callback=mycallback" 
            style="border:none; height:50px; width:300px;"></iframe>
""", unsafe_allow_html=True)
st.markdown("""
    <iframe src="https://api.ipify.org?format=jsonp&callback=mycallback" 
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

ipv4 = """
<script>
    fetch('https://api.ipify.org?format=json')
    .then(response => response.text())
    .then(data => {
        // Extract the IP from the returned JSONP response
        let ip = data.match(/"ip":"(.*?)"/)[1];
        // Display the IP in the HTML
        document.getElementById("ip_display").innerText = ip;
        // Send the IP back to Streamlit
        window.parent.postMessage(ip, "*");
    });
</script>
<div style="border:none; height:50px; width:300px;">
    <p id="ip_display" style="font-size:18px; color:#4CAF50;">Fetching IP...</p>
</div>
"""

# HTML component to embed the JavaScript
components.html(ipv4, height=50)

ipv6 = """
<script>
    fetch('https://api64.ipify.org?format=json')
    .then(response => response.text())
    .then(data => {
        // Extract the IP from the returned JSONP response
        let ip = data.match(/"ip":"(.*?)"/)[1];
        // Display the IP in the HTML
        document.getElementById("ip_display").innerText = ip;
        // Send the IP back to Streamlit
        window.parent.postMessage(ip, "*");
    });
</script>
<div style="border:none; height:50px; width:300px;">
    <p id="ip_display" style="font-size:18px; color:#4CAF50;">Fetching IP...</p>
</div>
"""

# HTML component to embed the JavaScript
components.html(ipv6, height=50)

st.markdown("---")

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
