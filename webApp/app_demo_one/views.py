from flask import Flask
app = Flask(__name__)
# app = Flask('app_demo_one')

# used . to import from same folder
# from .import views
# from . import app

@app.route('/home')
def home():
    return ('home page')

@app.route('/2')
def second_page():
    return ('You are on the second page')

if __name__=="__main__":
    app.run()
