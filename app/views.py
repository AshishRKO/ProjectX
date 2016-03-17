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
    print "Inside login"
    L=request.args.get('Language_Selector')
    return render_template('login.html')
    return "GO GO GO"
    print "List is "
    print L
    print type(L)

    code=request.form.get('json')
    print "Code ====================================================="
    print code
    print type(code)

    
    
    	#print form.openid.data
    res=False
    if(L=='java'):
    	print "JAVA running"
    	res= checkJAVA(str(code))
    elif(L=='c'):
    	print "C running"
    	res= checkC(str(code))
    else:
    	print "Nothing Running"
    	

    if(res==True):
        return redirect('/index')
    else:
        return redirect('/wrong')
    


    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
    
    return "Giving Response"


@app.route('/Processor', methods=['GET', 'POST'])
def Processor():
	print "Inside Processor function---------------------------"
	print request.form
	code=request.form['data']
	lang=request.form['Language_Selector']
	print code
	print type(code)
	

	print lang
	print type(lang)
	print str(lang)

	res=False
	if(lang=='java'):
		print "JAVA running"
		res= checkJAVA(str(code))
	elif(lang=='c'):
		print "C running"
		res= checkC(str(code))
	elif(lang=='c++'):
		print "C++ running"
		res=checkCpp(str(code))
	else:
		print "Nothing Running"
    	

	if(res==True):
		return redirect('/index')
	else:
		return redirect('/wrong')



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


def checkCpp(data):
	print "Checking C++ program"

	f = open("Main.cpp", "w")
	f.write(data)

	f.close()
	file = 'Main.cpp'
	lang='cpp'
	testin = 'testin.txt'
	testout = 'testout.txt'
	timeout = '1' # secs

	filename=file.split('.')[0]
	print(codes[frank.compile(file,lang)])
	print (codes[frank.run(filename,testin,timeout,lang)])
	res = frank.match(testout)
	print res

 	return res







