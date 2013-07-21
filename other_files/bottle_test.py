import bottle

@bottle.route('/hello/:name')
def index(name='World'):
    return template("<strong>Hello {{name}}</strong>",name=name)

@bottle.route('/testpage')
def test_page():
    return 'Test'

bottle.debug(True)

bottle.run(host='localhost',port=8180)

