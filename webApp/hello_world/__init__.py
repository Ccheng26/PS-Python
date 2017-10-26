# import flask, flask is the file from class Flask
from flask import Flask
# create instance of Flask
# gets value __main__, name __main__ is assigned to script when executed
app=Flask(__name__)

# maps function to route '/'
@app.route('/')
def hello_world():
    greeting="World"
    return f'Hello, {greeting}'

if __name__ == "__main__":
    app.run()