from routes import *
from models.user import  User
from models.comment import Comment
from models.node import Node
from models.topic import Topic

main = Blueprint('v2ex', __name__)


@main.route('/')
def v2ex():
    nodes = Node.query.all()
    node_name = [n.name for n in nodes]
    topics = []
    for n in node_name:
        node = Node.query.filter_by(name=n).first()
        print('node', n)
        topics += node.topics
    count = len(topics)
    for i in range(0, count):
        for j in range(i+1, count):
            if topics[i].created_time < topics[j].created_time:
                topics[i], topics[j] = topics[j], topics[i]
    # print('topics', topics)
    newest_topic = []
    if count > 10:
        for i in range(10):
            newest_topic.append(topics[i])
    else:
        newest_topic = topics
    # print('newest_topic', newest_topic)
    for t in newest_topic:
        t.comments_nums = len(t.comments)
    return render_template('v2ex_index.html', nodes=nodes, topics=newest_topic)


@main.route('/login')
def login():
    return render_template('user_login.html')


@main.route('/register')
def register():
    return render_template('user_register.html')
