

from flask import  Blueprint,current_app


user_blueprint = Blueprint("user_blueprint",__name__,url_prefix="/api/user")


@user_blueprint.route("/users")
def getUsers():

    return "user"
