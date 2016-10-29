from todoapp import app
'''Begin of todoapp application in python'''

@app.route('/')
def index():
	return '<h1>Hello World</h1>'