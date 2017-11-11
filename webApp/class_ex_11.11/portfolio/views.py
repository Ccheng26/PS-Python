from . import app
from flask import render_template, request, url_for

@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        return render_template('/redirect.html')
    elif request.method=='GET':
        return render_template('/index.html')

@app.route('/table')
def table():
    return render_template('/table.html')

# @app.route('/redirect')
# def redirect():
#     return render_template('/redirect.html')