from apps import db
import datetime

class Todo(db.Model):
   sno = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200), nullable=False)
   des = db.Column(db.String(800), nullable=True)
   date_created=db.Column(db.DateTime, default=datetime.utcnow)

   def __repr__(self) -> str:
      return f"{self.sno} - {self.title}"