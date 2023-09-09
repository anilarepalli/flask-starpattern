from flask import Flask,render_template,request
from pattern import logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/shape',methods=['post'])
def shape():
    choice = request.form['choice']
    value = request.form['value']
    result = logic(choice,value)
    return render_template("index.html",choice=choice,value=value,result=result)

if __name__ == '__main__':
    app.run(debug=True)