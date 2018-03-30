from flask import Flask, request, make_response, redirect, abort, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>', 200
	
@app.route('/user/<name>')
def user(name):
	user_agent = request.headers.get('User-Agent')
	return '<h1>Hello %s!</h1>' % name + '<p>Your browser is %s </p>' % user_agent, 200
	
	
@app.route('/cookie')
def cookie():
	# use make_response to create responses
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response
	
@app.route('/redirect')
def redir():
	#use redirect() to redirect
	return redirect('/redirected')
	
@app.route('/redirected')
def redirected():
	response = make_response('<h1>You have been redirected!</h1>')
	return response

if __name__ == '__main__':
	app.run(debug=True)