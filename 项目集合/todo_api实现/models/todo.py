from . import ModelMixin
from . import db
from . import StrfTime
import json

class Todo(db.Model, ModelMixin):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    time = db.Column(db.String())
    done = db.Column(db.Boolean)

    def __init__(self, form):
        self.task = form.get('task', '')
        self.done = form.get('done', False)
        self.time = StrfTime()

    def update(self, form):
        self.task = form.get('task', '')
        self.time = StrfTime()
        self.save()

    @classmethod
    def delete(cls, form):
        ts = cls.query.all()
        d = form.get('id')
        for t in ts:
            if t.id == d:
                t.delete()
        cls.save()

    def json(self):
        d = dict(
            id=self.id,
            task=self.task,
            done=self.done,
            time=self.time
        )
        return json.dumps(d)

