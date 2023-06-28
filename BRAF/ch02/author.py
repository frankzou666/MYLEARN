

from flask_sqlalchemy.model import Model
from flask_sqlalchemy import String,Column,Integer



class Author (Model):
    id = Column(Model, primary_key=True)
    name = Column(String(20))
    specialisation = Column(String(50))
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
    def __repr__(self):
      return '<Product %d>' % self.id