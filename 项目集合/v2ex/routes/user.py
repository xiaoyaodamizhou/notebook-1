from routes import *
from models.user import User
from models.topic import Topic

main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    status, error_messages = u.valid()
    print('status:{},messages:{}'.format(status, error_messages))
    if status:
        u.save()
        print('注册成功')
        return redirect(url_for('v2ex.v2ex'))
    else:
        # 用户
        return render_template('user_register_error.html', error=error_messages)


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        print('登陆成功')
        session['user_id'] = user.id
        return redirect(url_for('user.profile'))
    else:
        print('登录失败')
        error = '密码或用户名输入不对'
        return render_template('user_login_error.html', error=error)


@main.route('/user/update_password', methods=['POST'])
def update_password():
    u = current_user()
    password = request.form.get('password', '')
    if u.change_password(password):
        print('密码修改成功')
    else:
        print('密码修改失败')
    return redirect('/profile')


@main.route('/user/update_avatar', methods=['POST'])
def update_avatar():
    u = current_user()
    avatar = request.form.get('avatar', '')
    if u.change_avatar(avatar):
        print('图像修改成功')
    else:
        print('图像修改失败')
    return redirect('/profile')


@main.route('/profile', methods=['get'])
def profile():
    u = current_user()
    if u is not None:
        u = current_user()
        topics = list(u.topics)
        return render_template('profile.html', user=u, topics=topics)
    else:
        return redirect(url_for('user.login'))


@main.route('/topics')
def topics():
    u = current_user()
    topics = u.topics
    return render_template('user_topics.html', topics=topics)
