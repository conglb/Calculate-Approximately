from flask import Flask, render_template, request, redirect, url_for
from algo.system_of_equations.jacobi import solve
import numpy as np
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/sample.html')
def sample():
    return render_template('sample.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('home'))
        else:
            error = "Wrong password or username!"
    return render_template('login.html', error=error)

@app.route('/system-of-equations', methods=['GET', 'POST'])
def system_of_equations():
    ans = []
    if request.method == 'POST':
        # Read maxtrix from form
        variCount = int(request.args['v'])
        arr = []
        for i in range(variCount):
            arr.append([])
            for j in range(variCount):
                arr[i].append(request.form['x' + str(i+1) + ',' + str(j+1)])

        # Read vector form form
        vec = []
        for i in range(variCount):
            vec.append(request.form['b' + str(i+1)])
        app.logger.info(arr)
        timeOfIterations = request.form['time-of-iterations']
        ans = solve(np.array(arr), np.array(vec), timeOfIterations)
        return render_template('system-of-equations.html', ans=ans)
    return render_template('system-of-equations.html', ans=ans)

@app.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Check your console"

if __name__ == '__main__':
    app.debug = True
    app.run()
