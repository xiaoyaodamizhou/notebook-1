from utils import log
from models import Message
from models import Users

from response import session
from response import template
from response import response_with_headers
from response import redirect
from response import error

import random

message_list = []


def random_str():
    seed = "a1b3c2d5ef6g8hi9jkl3mn"
    s = ''
    for i in range(16):
        random_index = random.randint(0, len(seed) - 1)
        s += seed[random_index]
    return s


def current_user(request):
    session_id = request.cookies.get('user', '')
    username = session.get(session_id, "游客")
    return username


def route_index(request):
    header = 'HTTP/1.x 210 VERY OK\r\nContent-Type: text/html\r\n'
    username = current_user(request)
    body = template('index.html', username=username)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_login(request):
    headers = {
        'Content-Type': 'text/html',
    }
    log('login, headers', request.headers, request.method)
    username = current_user(request)
    if request.method == 'POST':
        form = request.form()
        u = Users(form)
        if u.validate_login():
            session_id = random_str()
            session[session_id] = u.username
            headers['Set-Cookie'] = 'user={}'.format(session_id)
            result = "登录成功"
        else:
            result = '没登录'
    else:
        result = ''
    log('result', result)
    body = template("login.html",
                    result=result,
                    username=username)
    header = response_with_headers(headers)
    r = header + '\r\n' + body
    log('body', body)
    return r.encode(encoding='utf-8')


def route_register(request):
    header = "HTTP/1.x 200 VERY OK\r\nContent-Type: text/html\r\n"
    if request.method == 'POST':
        form = request.form()
        u = Users(form)
        if u.validate_register():
            u.save()
            result = "注册成功<br> <pre>{}</pre>".format(Users.all())
        else:
            result = "用户名或者密码长度必须大于2"
    else:
        result = ''
    body = template("register.html", result=result)
    r = header + "\r\n" + body
    return r.encode(encoding='utf-8')


def route_message(request):
    headers = {
        'Content-Type': 'text/html',
    }
    log('本次请求的method', request.method)
    username = current_user(request)
    log('username', username)
    header = response_with_headers(headers)
    if request.method == "POST":
        form = request.form()
        message = Message(form)
        log('post', form)
        message_list.append(message)
    msgs = '<br>'.join(str(m) for m in message_list)
    body = template('html_basic.html', messages=msgs)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_profile(request):
    headers = {
        'Content-Type': 'text/html',
    }
    username = current_user(request)
    header = response_with_headers(headers)
    user = Users.find(username)
    body = template('profile.html', id=user.id,
                    username=user.name,
                    note=user.note)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_static(request):
    filename = request.query.get('file', 'doge.gif')
    path = '/Users/chen/Desktop/test/后端/serverConfig/static/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.x 200 OK\r\nContent-Typw: image/gif\r\n\r\n'
        img = header + f.read()
        return img


def login_required(function):
    def func(request):
        username = current_user(request)
        log("登录鉴定", username)
        if username == "游客":
            return redirect('/login')
        else:
            return function(request)

    return func


route_dict = {
    '/': route_index,
    '/login': route_login,
    '/register': route_register,
    '/messages': login_required(route_message),
    '/profile': login_required(route_profile),
}


