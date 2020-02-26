import json

from utils import log
import time


def save(data, path):
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        # log('save', path, s, data)
        f.write(s)


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        return json.loads(s)


class Model(object):
    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path = '/Users/chen/Desktop/test/后端/serverConfig/{}.txt'.format(classname)
        return path

    @classmethod
    def load(cls, d):
        m = cls({})
        for k, v in d.items():
            setattr(m, k, v)
        return m

    @classmethod
    def all(cls):
        path = cls.db_path()
        models = load(path)
        ms = [cls.load(m) for m in models]
        return ms

    @classmethod
    def find_by(cls, **kwargs):
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        _all = cls.all()
        for m in _all:
            if v == m.__dict__[k]:
                return m
        return None

    @classmethod
    def find_all(cls, **kwargs):
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        _all = cls.all()
        models = []
        if k != '':
            for m in _all:
                if v == m.__dict__[k]:
                    models.append(m)
        return models

    @classmethod
    def find(cls, id):
        return cls.find_by(id=id)

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} \n>\n'.format(classname, s)

    def save(self):
        models = self.all()
        if self.id is None:
            if len(models) == 0:
                self.id = 1
            else:
                m = models[-1]
                self.id = m.id + 1
            models.append(self)
        else:
            # index = self.find(self.id)
            index = -1
            for i, m in enumerate(models):
                if m.id == self.id:
                    index = i
                    break
            log('debug', index)
            models[index] = self
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)

    def delete(self):
        models = self.all()
        index = -1
        for i, m in enumerate(models):
            # log('debug', self, self.__dict__, m.__dict__)
            if self.id == m.id:
                index = i
                break
        del models[index]
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)

    def json_str(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


class Users(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.note = form.get('note', '')

    def validate_login(self):
        # return self.username == 'gua' and self.password == '123'
        u = Users.find_by(username=self.username)
        return u is not None and u.password == self.password

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2


class Message(Model):
    def __init__(self, form):
        self.id = None
        self.author = form.get('author', '')
        self.message = form.get('message', '')


class Weibo(Model):
    """
    """

    def __init__(self, form):
        # id 是独一无二的一条数据
        # 每个 model 都有自己的 id
        self.id = form.get('id', None)
        self.content = form.get('content', '')
        # int(time.time()) 得到一个 unixtime
        # unixtime 是现在通用的时间标准
        # 它表示的是从 1970.1.1 到现在过去的秒数
        # 因为 1970 年是 unix 操作系统创造的时间
        self.created_time = int(time.time())
        # 我们用 user_id 来标识这个微博是谁发的
        # 初始化为 None
        self.user_id = form.get('user_id', None)


class Comment(Model):
    def __init__(self, form):
        # id 是独一无二的一条数据
        # 每个 model 都有自己的 id
        self.id = form.get('id', None)
        self.content = form.get('content', '')
        # int(time.time()) 得到一个 unixtime
        # unixtime 是现在通用的时间标准
        # 它表示的是从 1970.1.1 到现在过去的秒数
        # 因为 1970 年是 unix 操作系统创造的时间
        self.created_time = int(time.time())
        # 我们用 user_id 来标识这个微博是谁发的
        # 初始化为 None
        self.user_id = int(form.get('user_id', -1))
        self.weibo_id = int(form.get('weibo_id', -1))


class Todo(Model):
    def __init__(self, form):
        # id 是独一无二的一条数据
        # 每个 model 都有自己的 id
        self.id = form.get('id', None)
        self.created_time = int(time.time())
        self.content = form.get('content', '')
        self.complete = False

    def toggleComplete(self):
        self.complete = not self.complete

    def status(self):
        return 'status-done' if self.complete else 'status-active'


def test_weibo():
    weibo_form = {
        'content': '今天天气很好'
    }
    w = Weibo(weibo_form)
    log(w.id, w.content, w.created_time)


def test():
    # users = User.all()
    # u = User.find_by(username='gua')
    # log('users', u)
    # form = dict(
    #     username='gua',
    #     password='gua',
    # )
    # u = User(form)
    # u.save()
    # log('u.id', u.id)
    # u3 = User.find(3)
    # u3.password = '123 789'
    # u3.save()
    # log('u3', u3)
    # log(User.all())
    test_weibo()


if __name__ == '__main__':
    test()
