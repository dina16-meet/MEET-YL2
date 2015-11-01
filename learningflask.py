from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash 
app = Flask(__name__)

@app.route("/")  
def home():
	return render_template('home.html') 

@app.route("/aboutme/")## creating the url /hello/ for that will run the following function
def aboutme(): 
	return render_template('aboutme.html')
@app.route("/contactme/")
def contactme(): 
	return render_template('aboutme.html')


@app.route("/contactme/", methods=['POST']) 
def contactme():
	  email = request.form['email'] ## in case the form used, then this is how we get the value that is written in the form
	  name = request.form ['name']
	return render_template('hello.html', email=email, name=name)## here telling flask to load the html code in hello.html with the variable name

## to create more urls and functions simple create them the same way created above just change what you need

if __name__ == "__main__": ## this if statement is telling python when running this file run the following lines
	app.debug = True ## this to let flask show us errors if there is any
	app.run() ## this tells python to run flask
