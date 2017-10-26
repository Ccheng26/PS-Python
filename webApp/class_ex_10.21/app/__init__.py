from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    information = "info"
    return render_template('index.html', information= informmation)

@app.route('/page1')
def page1():
    return 'Separate page:'

@app.route('/action.php')
def php():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
