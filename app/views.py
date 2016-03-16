from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm
import frank

import os
codes = {200:'success',404:'file not found',400:'error',408:'timeout'}


@app.route('/')
@app.route('/index')
def index():
    return "Correct Solutions"


@app.route('/wrong')
def wrong():
    return "Incorrect Solutions"



@app.route('/login', methods=['GET', 'POST'])
def login():
    L=request.args.get('Language_Selector')
    print "List is "
    print L
    print type(L)

    code=request.form.get('json')
    print "Code ====================================================="
    print code
    print type(code)

    
    form= LoginForm()
    if form.validate_on_submit():
    	#print form.openid.data
    	res=False
    	if(L=='java'):
    		print "JAVA running"
    		res= checkJAVA(form.openid.data)
    	elif(L=='c'):
    		print "C running"
    		res= checkC(form.openid.data)
    	else:
    		print "Nothing Running"
    	

        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        if(res==True):
        	return redirect('/index')
        else:
        	return redirect('/wrong')
    


    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
    
    return "Giving Response"




def checkJAVA(data):
	print "checking java program"
	
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


def checkC(data):
	print "Checing C program"

	f = open("Main.c", "w")
	f.write(data)

	f.close()
	file = 'Main.c'
	lang='c'
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








