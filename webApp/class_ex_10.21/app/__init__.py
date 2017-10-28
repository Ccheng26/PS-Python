from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def index():
    name = 'user'
    print(request.method)
    if request.method == 'POST':
        name= request.form['name']
        greet = request.form['greet']
        greetings = name + greet
    return render_template('index.html', greetings= greetings)

@app.route('/info')
def about():
    return render_template('info.html')
    
@app.route('/contact')
def contact():
    return "contact page"

if __name__ == "__main__":
    app.run(debug=True)
