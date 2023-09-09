from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/shape',methods=['post'])
def shape():

    return render_template('index.html',output=output)
if __name__ == '__main__':
    app.run(debug=True)