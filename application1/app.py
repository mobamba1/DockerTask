from flask import Flask, render_template, Response 
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  
  return render_template('home.html', title='Home' )

@app.route('/generate')
def generate():
  data = requests.get('http://35.246.3.155:5001/animals/noise')
  output = data.text
  
  return render_template('generate.html', post=output, title='Genrate' )


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
