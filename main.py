from bottle import route, run

@route('/')
def index():
    return '<b>Hello world!</b>'

run(host='localhost', port=8080)