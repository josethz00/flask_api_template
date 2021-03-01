from datetime import datetime
from dataclasses import dataclass

from src.shared.database.db import db


@dataclass
class User(db.Model):

    id: int
    username: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime(),
        default=datetime.utcnow(),
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime(),
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
        nullable=False
    )

    def __repr__(self):
        return '<User %r>' % self.id
