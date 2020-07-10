from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        a = float(request.form['altura'])
        p = float(request.form['peso'])
        r = p/(a*a)
        return render_template('result.html', r=r)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)