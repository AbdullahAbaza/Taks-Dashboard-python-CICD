from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
        }