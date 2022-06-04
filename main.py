from flask import Flask,  render_template, request
from waitress import serve

from datetime import datetime

from isvalid import isvalid
from isadmin import isadmin

now = datetime.now()

currenttime = now.strftime("%H:%M:%S")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/demo/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        code=request.form['usercode']
        name=request.form['username']
        isvalid.isvalid(name, code)
        with open('data/response.txt') as f:
          response = f.read()
        time=currenttime
        with open('templates/demo/info.json', 'w') as f:
            f.write('{"Name": "' + name + '", "Code": "' + code + '", "Time": "' + time + '"}')
        return render_template('demo/data.html', code=request.form['usercode'], name=request.form['username'], time=currenttime, response=response)
    elif request.method == 'GET':
        return render_template('demo/redirecthome.html')
    else:
        return 'Not a valid request method for this route' 


@app.route('/json')
def json():
    return render_template('demo/info.json')

@app.route('/home')
def backhome():
    return render_template('homepage.html')
@app.route('/demo/home')
def demohome():
    return render_template('demo/home.html')
@app.route('/data')
def welcome():
    return render_template('demo/data.json')
@app.route('/demo/admin')
def admin():
    return render_template('demo/admin.html')
@app.route('/demo')
def demo():
    return render_template('demo/home.html')


@app.route('/demo/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        code=request.form['usercode']
        name=request.form['username']
        isadmin.isadmin(name, code)
        with open('data/response.txt') as f:
          response = f.read()
        time=currenttime
        with open('templates/info.json', 'w') as f:
            f.write('{"Name": "' + name + '", "Code": "' + code + '", "Time": "' + time + '"}')
        return render_template('demo/adminhome.html', name=request.form['username'], time=currenttime, response=response)
    elif request.method == 'GET':
        return render_template('demo/redirecthome.html')
    else:
        return 'Not a valid request method for this route' 



@app.route('/demo/admin/logs', methods=['GET', 'POST'])
def logs():
    if request.method == 'POST':
      return render_template('demo/logs.txt')
    elif request.method == 'GET':
        return render_template('demo/redirectadmion.html')
    else:
        return 'Not a valid request method for this route' 



@app.route('/workscited')
def workscited():
  return render_template('workscited.html')

#error pages

@app.errorhandler(404)
def not_found(fourofour):
  return render_template("404.html")
  

@app.errorhandler(500)
def server_error(fivehundred):
  return render_template("500.html")


if __name__ == "__main__":
    print('Website Alive')
    serve(app, host='0.0.0.0', port=5000)