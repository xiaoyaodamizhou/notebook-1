from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

def StrfTime():
    value = time.localtime(int(time.time()))
    dt = time.strftime('%Y/%m/%d %H:%M:%S', value)
    print('error, dt', dt)
    return dt

class ModelMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        className = self.__class__.__name__
        properties = ('{}={}'.format(k, v) for k, v in self.__dict__.items())
        return '<{}:\n({})\n>'.format(className, '\n'.join(properties))


