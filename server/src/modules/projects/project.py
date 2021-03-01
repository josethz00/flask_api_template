from datetime import datetime

from src.shared.database.db import db


class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
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

    task = db.relationship(
        'Task',
        backref='projects',
        cascade='all, delete-orphan',
        uselist=True
    )

    def __repr__(self):
        return '<Project %r>' % self.id
