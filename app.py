#import eventlet
#from eventlet import wsgi

from server import app

if __name__ == '__main__':

    app.debug = True
    app.run(host='0.0.0.0', port=84)
    #wsgi.server(eventlet.listen(('', 84)), app)
