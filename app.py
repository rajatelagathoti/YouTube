from flask import Flask, request 
app = Flask(__name__)
def home():
  return open("index.html").read()
app.run(debug = True)
