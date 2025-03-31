

from flask import  Blueprint,current_app
from ..models.user import User


admin_blueprint = Blueprint("admin_blueprint",__name__,url_prefix="/api/admin")


@admin_blueprint.route("/users")
def getUsers():
    user=User()
    user.username="hello"
    user.password="good"
    current_app.db.session.add(user)
    current_app.db.session.commit()
    return "addmin"

