# FROM CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request, url_for
# INDEX ROUTE AND FUNCTION(FOR PAGE)

comments=[{'name':'p1', 'message':'Happy Halloween!'},
          {'name':'p2', 'message':"Halloween is over..."}]
# comments=['test1', 'test2']

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/about', methods=['GET','POST'])
def about():
    if request.method =='POST':
        return render_template('/confirm.html')
    if request.method =='GET':
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

secret= 3
store=[]
@app.route('/cipher', methods=['GET','POST'])
def cipher():
    if request.method =='POST':
        phrase= request.form['phrase']
        encrypted= list()
        for char in phrase:
            encrypted.append(chr(ord(char)+secret))
        encrypted_string="".join(encrypted)
        if not store:
            store.append({'in_phrase':phrase, 'encrypted_p':encrypted_string})
        else:
            store[0]={'in_phrase':phrase, 'encrypted_p':encrypted_string}
        print(store)
        return render_template('/cipher.html', encrypted= store)
    if request.method=='GET':
        store.clear()
        return render_template('cipher.html', encrypted= store)
