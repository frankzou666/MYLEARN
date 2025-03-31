import time

from flask import  Flask,jsonify,request,current_app,g
from flask_socketio import  SocketIO,emit,send
from flask_cors import CORS
from threading import Thread

app = Flask(__name__)
# 2.2.3 以前的版本app.config['JSON_AS_ASCII'] = False
app.json.ensure_ascii = False

app.app_context().push()

socketio = SocketIO(app=app)

socketio = SocketIO(app,cors_allowed_origins="*")
cors = CORS(app, resources={r"/*": {"origins": "*"}},supports_credentials=True)


WS_NAMESPACE='/interfacecheck'
@app.route("/api/getIndex/",methods=['get'])
def getIndex():
    currentPage = request.args.get('currentPage')
    pageSize = request.args.get('pageSize')
    data = (
            {
                'interfaceName': '/A',
                "interfaceId": 1,
                'lastCheckTime': '2024-04-21 21:00:05',
                'lastAvg10': 1.2,
                'lastAvg5': 2,
                'lastAvg3': 0.03,
                'lastAvg1': 1.5,
                'lastResponseTime': 1,
                'interfaceDesc': '这是一个很重要的接口',
                'autoCheckStatus': True,
            },
            {
                'interfaceName': '/B',
                "interfaceId": 3,
                'lastCheckTime': '2024-04-21 21:00:05',
                'lastAvg10': 1.2,
                'lastAvg5': 2,
                'lastAvg3': 3,
                'lastAvg1': 2,
                'lastResponseTime': 1.2,
                'interfaceDesc': '这是一个很重要的接口',
                'autoCheckStatus': False,

            },
            {
              'interfaceName': '/C',
              "interfaceId": 9,
              'lastCheckTime': '2024-04-21 21:00:05',
              'lastAvg10': 3.8,
              'lastAvg5': 2,
              'lastAvg3': 13.003,
              'lastAvg1': 1,
              'lastResponseTime': 3.2,
              'interfaceDesc': '这是一个很重要的接口1',
              'autoCheckStatus': True,
            }
    )
    total = 20;
    return  jsonify({'code':200, 'data':{'total':total,'currentPage':currentPage,'pageSize':pageSize,'items':data}})


@app.route("/api/updateIntOnOFF",methods = ['POST'])
def updateIntOnOFF():
    """
         更新单个接口的开或关
         需要付入参数: interface_id
    :return:
    """
    interface_id = request.get_json().get("interfaceId")
    autoCheckStatus = request.get_json().get("autoCheckStatus")
    ip=request.remote_addr
    print(int(autoCheckStatus))
    return jsonify({'code': 200, 'data': []})



@app.route("/api/getInterfaceResponse",methods = ['POST'])
def getInterfaceResponse():
    """
         返回单个接口响应时间
         需要付入参数: interface_id
    :return:
    """
    interface_id = request.get_json().get("interfaceId")
    ip=request.remote_addr

    if not interface_id:
        return jsonify({'code': 10001, 'success': False, 'msg': 'PARAM_ERROR_INTERFACE_ID'})
    return jsonify({'code': 200, 'data': []})

@app.route("/api/getInterfaceLast10",methods = ['POST'])
def getInterfaceLast10():
    """
         返回单个最后10次响应时间
         需要付入参数: interface_id
    :return:
    """
    interface_id = request.get_json().get("interfaceId")
    ip=request.remote_addr

    if not interface_id:
        return jsonify({'code': 10001, 'success': False, 'msg': 'PARAM_ERROR_INTERFACE_ID'})
    charDataX = [
        '16:28:29',
        '16:18:29',
        '16:08:29',
        '15:58:29',
        '15:48:29',
        '15:38:29',
        '15:28:29',
        '15:18:29',
        '15:08:29',
        '14:58:29',

    ]
    charDataY = [
        3.1,
        3.4,
        3.0,
        2.9,
        2.9,
        3.0,
        3.1,
        3.0,
        3.0,
        3.0
    ]
    return jsonify({'code': 200, 'data': {'charDataX':charDataX,'charDataY':charDataY}})

@app.route("/api/checkInterfaceAll",methods = ['POST'])
def checkInterfaceAll():
    """
         手动检测所有接口
         需要付入参数: interface_id
    :return:
    """
    ip=request.remote_addr
    emit('operationEvent', {'operationType':'getIndex'},namespace=WS_NAMESPACE,broadcast=True)
    return jsonify({'code': 200, 'data': []})



def getFreashAndCheckTime():
    with app.app_context():
        autoCheckSeconds = 0
        autoFreashSeconds = 15
        while 1:
            time.sleep(1)
            autoCheckSeconds = autoCheckSeconds - 1
            autoFreashSeconds = autoFreashSeconds -1
            data = {'operationType': 'getFreashAndCheckTime', 'autoCheckSeconds': autoCheckSeconds,
                    'autoFreashSeconds': autoFreashSeconds}
            emit('operationEvent', data, namespace=WS_NAMESPACE, broadcast=True)
            if autoFreashSeconds == 0:
                emit('operationEvent', {'operationType': 'getIndex'}, namespace=WS_NAMESPACE, broadcast=True)
                autoFreashSeconds = 15



@socketio.on('connect',namespace=WS_NAMESPACE)
def connectSocket():
    pass



@socketio.on('disconnect',namespace=WS_NAMESPACE)
def disconnectSocket():
    emit(event='hello',broadcast=True)


def main():
    Thread(target=getFreashAndCheckTime).start()
    socketio.run(app=app,host="0.0.0.0",port=8889,allow_unsafe_werkzeug=True ,debug=True)


if __name__=="__main__":
    main()