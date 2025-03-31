

from flask import current_app,render_template




def index():
    return  render_template("index.html"),200