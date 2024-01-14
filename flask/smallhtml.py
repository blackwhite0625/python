from flask import Flask ,request,render_template, url_for , redirect ,flash
#import url_for,redirect
#from flask import render_template

app = Flask(__name__)

#flack支援str,int,float,path
#@app.route('/')
#def index():
#    return 'hellllooooo'
#@app.route('/user/<username>')
#def username(username):
#    return 'i am '+ username
#@app.route('/age/<int:age>')
#def userage(age):
#    return 'i am '+ str(age) + 'years old'


#url_for使用
#@app.route('/a')
#def url_for_a():
#    return 'here is a'
#@app.route('/b')
#def b():
    #redirect搭配url_for 引導進另一個路由 避免調整路由要整個專案去調整
    #redirect
#    return redirect (url_for('url_for_a'))


#render_template用法
#@app.route('/para/<user>')
#def index(user):
#    return render_template('abc.html',user_template=user)


#request 處理 method get post 
#@app.route('/login',methods=['GET','POST'])
#def login():
#    if request.method == 'POST':
#        return 'Hello ' + request.values['username']
    
#    return "<form method='post' action='/login'> <input type='text' name='username' />"\
#            "<br>"\
#           "<button type='submit'> Submit </button></form>"


#html url_for代替action
#@app.route('/loginurl',methods=['POST','GET'])
#def login():
#    if request.method == 'POST':
#        return 'Hello ' + request.values['username']
#    return render_template('login.html')


#redrect配合url_for用法
#@app.route('/loginurl',methods=['POST','GET'])
#def login():
#   if request.method == 'POST':
#        return redirect (url_for('hello',username=request.form.get('username')))
#        #return redirect (url_for('hello',request.form.get('Your Parameter')))
#    return render_template('login.html')

#@app.route('/hello/<username>')
#def hello(username):
#    return render_template('hello.html',username=username)


#flash message使用
@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('登錄成功!')
            return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')

#檢查登錄帳號密碼
def login_check(username, password):
    if username == 'admin' and password == 'hello': #輸入帳號密碼
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your key"#加密
    app.run()

