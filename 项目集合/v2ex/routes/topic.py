from models.topic import Topic
from models.node import Node
from routes.user import current_user
from routes import *

main = Blueprint('topic', __name__)

Model = Topic


# @main.route('/')
# def index():
#     ms = Model.query.all()
#     return render_template('topic_index.html', node_list=ms)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    topic_comments = len(m.comments)
    return render_template('topic.html', topic=m, topic_comments=topic_comments)


@main.route('/edit/<id>')
def edit(id):
    t = Model.query.get(id)
    u = current_user()
    # 等下修改
    # u.change_topics()
    return render_template('topic_edit.html', topic=t)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.node_id = int(form.get('node_id'))
    m.user_id = int(form.get('user_id'))
    m.save()
    node_id = m.node_id
    n = Node.query.get(node_id)
    return redirect(url_for('node.show', id=n.id))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('topic.show', id=t.id))


@main.route('/delete/<int:id>')
def delete(id):
    t = Model.query.get(id)
    # 单个话题没了的话肯定是返回到该用户的所有话题页面
    # 但是呢，对应用户删除对应用户的文章，不可越界
    t.delete()
    u = current_user()
    topics = u.topics
    return redirect(url_for('user.topics'))
