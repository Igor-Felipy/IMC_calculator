from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='templates')


@app.route('/', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        a = float(request.form['altura'])
        p = float(request.form['peso'])
        r = round( p/(a*a), 2)
        return render_template('result.html', r=r)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)