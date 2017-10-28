# FROM CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request, url_for
# INDEX ROUTE AND FUNCTION(FOR PAGE)

comments=[{'name':'p1', 'message':'Happy Halloween!'},
          {'name':'p2', 'message':"It's not halloween yet..."}]
# comments=['test1', 'test2']

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/commentchannel', methods=['GET','POST'])
def commentchannel():
    if request.method =='POST':
        name_add= request.form['name']
        message_add= request.form['message']
        comments.append({'name':name_add, 'message':message_add})
        print(comments)
        return render_template('/commentchannel.html', messages= comments)
    elif request.method=='GET':
        print(comments)
        return render_template('commentchannel.html', messages= comments)