import requests 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    myip = requests.get("http://myexternalip.com/raw").text
    return f"<h1><p style='font-family:monospace'>This is My IP {myip}</p></h1><br><h1><p style='font-family:monospace'>This VPN service is running from <a href='https://github.com/MrxAravind/paas-vpn'>this source code</a></p></h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
