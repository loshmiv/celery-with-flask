from .database import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    @property
    def get_name(self):
        return {
            'name': self.name
        }
