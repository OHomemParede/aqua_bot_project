from flask import Flask
from threading import Thread

app = Flask(__name__)

def send_ok():
  app.run(host='0.0.0.0', port=8080)
  
@app.route('/')
def index():
  return "OK"


Thread(target=send_ok, args=()).start()
