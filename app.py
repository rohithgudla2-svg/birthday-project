from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "Ruchi"
PASSWORD = "Ruchi1432"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if user == USERNAME and pwd == PASSWORD:
            return redirect(url_for('home'))
        else:
            return "Wrong login 😅"

    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('oldindex.html')

@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)