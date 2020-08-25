from flask import Flask, render_template, redirect, request, url_for
import back, main

from glob import glob
file_list = glob("main.py")

app = Flask(__name__)

@app.route('/')
@app.route('/<obj>')
def inputText(obj=None):
    print("in inputText funct, obj : ", obj)
    return render_template('main.html', obj=obj)

@app.route('/translate', methods=['POST'])
def translate(obj=None):
    if request.method == 'POST':
        temp = request.form['obj']
        if temp == "bird":
            print("RUN MACHINE!!!!")
            main.run_machine()
            print("AFTER MACHINE RUN, OBJ : ", temp)
            return redirect(url_for('inputText', obj=temp))
        elif temp == "붉은 털을 가진 여우":
            print("RUN MACHINE!!!!")
            main.run_machine()
            print("AFTER MACHINE RUN, OBJ : ", temp)
            return redirect(url_for('inputText', obj=temp))
    else:
        temp = None
    print("in translate funct, temp : ", temp)

    return redirect(url_for('inputText',obj=temp))

if __name__ == '__main__':
    print("============================START==========================")
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # main.run_machine()
    app.run()

