from models.node import Node
from models.topic import Topic
from models.user import User
from routes.user import current_user
from flask import abort
from routes import *

# for decorators
from functools import wraps

main = Blueprint('node', __name__)

Model = Node


# def admin_required(f):
#     @wraps(f)
#     def function(*args, **kwargs):
#         if request.args.get('uid') != 1:
#             print('not admin')
#             abort(404)
#         return f(*args, **kwargs)
#     return function


def admin_required():
    u = current_user()
    if u is None:
        abort(404)
    if u.id == 1:
        return True
    else:
        return False


@main.route('/')
def index():
    u = current_user()
    if u.id == 1:
        ms = Model.query.all()
        return render_template('node_index.html', node_list=ms)
    else:
        abort(404)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    u = current_user()
    node_topics_num = len(m.topics)
    return render_template('node.html', node=m, user=u, topics_num=node_topics_num)


@main.route('/edit/<id>')
# @admin_required(uid)
def edit(id):
    if admin_required():
        t = Model.query.get(id)
        return render_template('node_edit.html', node=t)


@main.route('/add', methods=['POST'])
# @admin_required()
def add():
    if admin_required():
        form = request.form
        m = Model(form)
        m.save()
        return redirect(url_for('.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
# @admin_required(uid)
def delete(id):
    if admin_required():
        t = Model.query.get(id)
        t.delete()
        return redirect(url_for('.index'))
