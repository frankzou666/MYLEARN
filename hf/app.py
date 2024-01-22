
from flask import Flask,render_template,request

# configuration
app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 9090
DEBUG=True

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/ch303",methods=["GET","POST"])
def ch101():
    parms = request.form
    print(parms)
    return render_template("ch304.html")


@app.route("/ch102",methods=["GET","POST"])
def ch202():
    parms = request.form
    print(parms)
    return render_template("ch102fruit.html")

@app.route("/fruit",methods=["GET","POST"])
def fruit():
    parms = request.form
    print(parms)
    return render_template("ch102fruit.html")





if __name__ == '__main__':
    app.run(host=HOST,port=PORT,debug=DEBUG)
