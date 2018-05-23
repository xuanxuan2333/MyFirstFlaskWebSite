from app import app
from flask import render_template, redirect, flash
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	title = 'index'
	user = {'nickname' : 'xuanxuan'}
	posts = [
		{'name': 'lxr','body':'1231123'},
		{'name' : 'zj', 'body':'456456'}	
	]
	return render_template('index.html', title = title, user = user, posts = posts)

@app.route('/login', methods = {'GET' , 'POST'})
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash("Login request for openid= " + form.openid.data + ", remember_me = " + str(form.remember_me.data))
		return redirect("/index")
		
	return render_template('login.html', title = "Sign In", form = form, providers = app.config['OPENID_PROVIDERS']) 	
