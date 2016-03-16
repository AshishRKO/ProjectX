from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
import frank

import os
codes = {200:'success',404:'file not found',400:'error',408:'timeout'}


@app.route('/')
@app.route('/index')
def index():
    return "Correct Solutions"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	print form.openid.data
    	res= check(form.openid.data)
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        if(res==True):
        	return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])




def check(data):
	print "check"
	

	f = open("Main.java", "w")
	f.write(data)

	f.close()
	file = 'Main.java'
	lang='java'
	testin = 'testin.txt'
	testout = 'testout.txt'
	timeout = '1' # secs

	filename=file.split('.')[0]
	print(codes[frank.compile(file,lang)])
	print (codes[frank.run(filename,testin,timeout,lang)])
	  # T
	res = frank.match(testout)
	print res

 	return res










