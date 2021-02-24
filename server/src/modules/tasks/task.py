from datetime import datetime

from src.shared.database.db import db


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
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
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=True
    )
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('projects.id'),
        nullable=False
    )

    def __repr__(self):
        return '<Task %r>' % self.id
