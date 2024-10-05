from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('healthcheck.html')

@app.route('/healthcheck')
def healthcheck():
    return render_template('healthcheck.html')

@app.route('/relogio1')
def reloj1():
    return render_template('reloj1.html')

@app.route('/relogio2')
def reloj2():
    return render_template('reloj2.html')

@app.route('/relogio3')
def reloj3():
    return render_template('reloj3.html')

if __name__ == '__main__':
    app.run(debug=True)