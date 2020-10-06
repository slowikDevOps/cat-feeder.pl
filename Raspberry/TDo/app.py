import socketio
import naclick
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)


sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    logging.info('connection established')
@sio.on('engine')
def on_message(data):
    naclick.start()
    print('I received a message! - engine')
    logging.info('The cat was feed!')

@sio.on('onlight')
def on_message(data):
    naclick.onswitch()
    print('I received a message! - onlight')
    logging.info('Light on!')

@sio.on('offlight')
def on_message(data):
    naclick.offswitch()
    print('I received a message! - offlight')
    logging.info('Light off!')

@sio.event
def disconnect():
    print('disconnected from server')
    logging.info('Disconnect')

sio.connect('http://cat-feder.pl')
sio.wait()
