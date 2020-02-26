from . import ModelMixin
from . import db
from . import timestamp
# from models.user import User

class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    created_time = db.Column(db.String())
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.comment = form.get('comment')
        self.created_time = timestamp()

    def valid(self):
        return len(self.comment) > 0

    def error_message(self):
        if len(self.comment) <= 2:
            return '评论太短，至少要3个字符'
        elif len(self.comment) >= 100:
            return '评论太长,要小于99个字符'

    # 待解决
    def json(self):
        d = dict(
            id=self.id,
            comment=self.comment,
            created_time=self.created_time,
        )
        return d