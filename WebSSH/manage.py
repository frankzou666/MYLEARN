
import time

from flask import  Flask,jsonify,request,current_app,g
from flask_socketio import  SocketIO,emit,send
from flask_cors import CORS
import paramiko

NAME_SPACE='/term'


app = Flask(__name__)
# 2.2.3 以前的版本app.config['JSON_AS_ASCII'] = False
app.json.ensure_ascii = False

app.app_context().push()

socketio = SocketIO(app=app)

socketio = SocketIO(app,cors_allowed_origins="*")
cors = CORS(app, resources={r"/*": {"origins": "*"}},supports_credentials=True)


def sshClient():
    tran = paramiko.Transport(('192.168.1.146', 22,))
    tran.start_client()
    tran.auth_password('root', 'rootroot')
    chan = tran.open_session()
    chan.get_pty()
    chan.invoke_shell()
    return  chan


sessionSsh = sshClient()
#接收客户端的信息
@socketio.on('clientMessage',namespace=NAME_SPACE)
def getClientMessage(message):
    clientCmd = message.get('data')
    if clientCmd is not None:
        sessionSsh.send(clientCmd+'\n')
        time.sleep(1)
        result = sessionSsh.recv(9999)
        socketio.emit('clientResponse',{'data':result.decode('utf-8')},namespace=NAME_SPACE)


    #发送数据到客户端
@socketio.on('clientResponse',namespace=NAME_SPACE)
def getClientResponse(): 
    pass


@socketio.on('connect',namespace=NAME_SPACE)
def getConnection():
    result = sessionSsh.recv(4096)
    socketio.emit('clientResponse', {'data': result.decode('utf-8')}, namespace=NAME_SPACE)
    print('connection')


@socketio.on('disconnect',namespace=NAME_SPACE)
def disconnect():
    print('disconnect')

def main():
    socketio.run(app=app,host="0.0.0.0",port=9999,allow_unsafe_werkzeug=True ,debug=True)


if __name__=="__main__":
    main()