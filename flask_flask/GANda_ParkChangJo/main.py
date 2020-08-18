from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<int:num>')
def inputLearn(num=None):
    return render_template('main.html', num=num)

@app.route('/calculate', methods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('inputLearn',num=temp))

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
