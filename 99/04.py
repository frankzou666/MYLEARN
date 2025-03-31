import os
from PIL import Image
from pyzbar.pyzbar import decode
from flask import Flask, request, jsonify,render_template

app = Flask(__name__,static_folder='statics')


def index():
    return  render_template('1.html')

@app.route('/code',methods=['POST'])
def decode_qr_code():
    file = request.files['file']
    save_path = 'c:/tmp'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    img_path = os.path.join(save_path + '/' + file.filename)
    file.save(img_path)
    image = Image.open(img_path)
    decoded_objects = decode(image)
    data = ""
    for obj in decoded_objects:
        print("Data:",obj.data.decode("uft-8"))
        data = obj.data.decode("uft-8")
        os.remove(img_path)

    return jsonify({'data': data, 'msg': 'ok','status':0})

if __name__=='__main__':
     app.run(host='0.0.0.0',port=5001)