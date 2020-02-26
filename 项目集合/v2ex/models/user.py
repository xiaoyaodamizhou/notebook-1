import hashlib
import os

from . import ModelMixin
from . import db
from models.topic import Topic
from models.comment import Comment


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    avatar = db.Column(db.String())
    topics = db.relationship('Topic', backref='user')
    comments = db.relationship('Comment', backref='user')

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.avatar = form.get('avatar', '/static/img/default.gif')
        self.topics_num = len(self.topics)

    # 验证注册用户的合法性的
    def valid(self):
        valid_username = User.query.filter_by(username=self.username).first()
        valid_username_len = len(self.username) >= 2
        valid_password_len = len(self.password) >= 3
        msgs = []
        if valid_username is not None:
            message = '用户已存在'
            print('user is:{}'.format(valid_username))
            msgs.append(message)
        elif not valid_username_len:
            message = '用户名长度要大于2'
            msgs.append(message)
        elif not valid_password_len:
            message = '用户名密码要大于24'
            msgs.append(message)
        status = (valid_username is None) and valid_username_len and valid_password_len
        return status, msgs

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password

    def change_password(self, password):
        if len(password) > 2:
            self.password = password
            self.save()
            return True
        else:
            return False

    def change_avatar(self, avatar):
        if len(avatar) > 2:
            self.avatar = avatar
            self.save()
            return True
        else:
            return False

    def change_topics(self, topics):
        self.topics = topics
        self.topics = str(self.topics)
        self.save()
