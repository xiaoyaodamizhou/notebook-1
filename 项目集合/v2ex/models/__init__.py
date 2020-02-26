from flask_sqlalchemy import SQLAlchemy
from flask import session
import time

db = SQLAlchemy()


def timestamp():
    formats = '%Y/%m/%d %H:%M:%S'
    dt = time.localtime(int(time.time()))
    value = time.strftime(formats, dt)
    return value


class ModelMixin(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{} = {}'.format(k, v) for k, v in self.__dict__.items())
        return '{}\n{}\n'.format(class_name, '\n'.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
