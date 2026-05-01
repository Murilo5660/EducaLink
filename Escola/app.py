from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_aluno')
def aluno():
    return render_template('login_aluno.html')

@app.route('/login_professor')
def professor():
    return render_template('login_professor.html')

if __name__ == '__main__':
    app.run(debug=True)
