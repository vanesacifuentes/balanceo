from flask import Flask
import requests

app = Flask(__name__)


global port
port=0

@app.route('/')

def index():
    
    global port
    
    if port==0:
        r = requests.get('http://127.0.0.1:3000/')
        port=1
    else:
        r= requests.get('http://127.0.0.1:3001/')
        port=0    
    
    data= r.text
    return data
  



if __name__ == '__main__':
    app.run(debug=True)