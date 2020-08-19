  
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import random, string
import requests



app = Flask(__name__)

@app.route('/animals', methods=['GET'])
def animals():
  list1=['Dog', 'Cat']
  b=random.randint(0,1)
  return Response(list1[b], mimetype='text/plain')

@app.route('/animals/noise', methods=['GET','POST'])
def animalsnoises():
  data = requests.get('http://35.246.3.155:5001/animals')
  output =""
  if data.text == "Dog":
    output = data.text + " Woof"
  else:
    output = data.text + " Mweoh"
  return Response(output, mimetype='text/plain')





if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)
