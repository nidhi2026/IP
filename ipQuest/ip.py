import streamlit as st
import streamlit.components.v1 as components
import requests

def extract_ip_address(data):
    try:
        json_string = data.decode('utf-8')
        json_data = json.loads(json_string)
        return json_data.get('ip')
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Error extracting IP address: {e}")
        return None

def fetch_ip_address(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return extract_ip_address(response.content)
    else:
      print("Error fetching ip address")

  except requests.exceptions.RequestException as e:
    print(f"Error fetching IP: {e}")
    return None

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
    fetch('https://api.ipify.org?format=jsonp&callback=mycallback')
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
components.html(ipv4, height=100)

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
components.html(ipv6, height=100)

