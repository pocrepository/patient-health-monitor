from flask import Flask,render_template,url_for,request, make_response
import random 
import json
from time import time
from random import uniform


app = Flask(__name__)        

@app.route('/', methods=["GET","POST"])
def  main():
	return render_template('result.html')
	
@app.route('/data',methods=["GET","POST"])
def data():

	data = [time() * 1000, uniform(98,99)]
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response

@app.route('/data2',methods=["GET","POST"])
def data2():

	data = [time() * 1000, uniform(65,80)]
	response = make_response(json.dumps(data))
	response.content_type = 'application/json'
	return response	
	

if __name__ == '__main__':
	app.run(debug=True)
