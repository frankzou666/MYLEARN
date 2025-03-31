
from flask import  Flask,jsonify
from flask_cors import cross_origin,CORS




app = Flask(__name__)
CORS(app)


@app.route('/hello')
def Hello():
    jsonStr = {"total":0,"limit":50,"skip":0,"data":[]}
    return jsonify(jsonStr)

@app.route('/contacts',methods=['GET'])
def getContacts():
    jsonStr = {"total":0,"limit":50,"skip":0,"data": [
    {
      "_id": "1",
      "name": {
        "first":"John1",
        "last":"Doe"
      },
      "phone":"555",
      "email":"john@gmail.com"
    },
    {
      "_id": "2",
      "name": {
        "first":"Bruce",
        "last":"Wayne"
      },
      "phone":"777",
      "email":"bruce.wayne@gmail.com"
    }
]    }
    return jsonify(jsonStr)
def main():
    app.run(host="0.0.0.0",port=9000)

if __name__ == '__main__':
    main()