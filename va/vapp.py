
from flask import Flask,render_template,request

# configuration
app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 9091
DEBUG=True

@app.route("/hello")
def hello():
    return render_template("hello.html")








if __name__ == '__main__':
    app.run(host=HOST,port=PORT,debug=DEBUG)
