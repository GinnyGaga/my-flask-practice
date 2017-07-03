from flask import Flask  
app=Flask(__name__) 


@app.route('/') 
def index():
	return '<h1>Index Page</h1>'

@app.route('/hello')
def hello(): 
	return "<h1>Hello World!I am ginny.</h1>" 

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Subpath %s' % subpath
