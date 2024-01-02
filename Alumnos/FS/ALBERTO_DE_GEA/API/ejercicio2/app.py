from flask import Flask, redirect, url_for, render_template, request, flash
 
app = Flask(__name__,template_folder='templates')
 
app.debug = True


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return f'welcome to a POST of {user}'
   else:
      return 'welcome to a GET'
 
@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        return 'You are running GET method for '+ user_id + ' user'
    if request.method == 'POST':
        return 'You are running POST method for '+ user_id + ' user ' 
    if request.method == 'DELETE':
        return 'You are running DELETE method for '+ user_id + ' user '

@app.get('/Users/<users_id>')
def getUser(user_id):
    return 'You are running PUT method for '+ user_id +' user '

@app.post('/Users/<users_id>')
def postUser(user_id):
    return 'You are running PUT method for '+ user_id +' user '

@app.delete('/Users/<users_id>')
def deleteUser(user_id):
    return 'You are running PUT method for '+ user_id +' user '

@app.put('/Users/<users_id>')
def putUser(user_id):
    return 'You are running PUT method for '+ user_id +' user '

app.run(host='0.0.0.0' , port=99)
