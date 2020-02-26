from routes import *
from models.comment import Comment
from models.topic import Topic
from models.user import User
from routes.user import current_user
import json

main = Blueprint('comment', __name__)
Model = Comment

@main.route('/comment/add', methods=['post'])
def add_comment():
    form = request.form
    # print('ajax发过来的内容是:{}'.format(form))
    u = current_user()
    c = Model(form)
    c.user_id = u.id
    c.topic_id = form.get('topic_id')
    r = {
        'data': []
    }
    if c.valid():
        c.save()
        r['success'] = True
        data = c.json()
        u = User.query.get(c.user_id)
        t = Topic.query.get(c.topic_id)
        # print('topic', t.title)
        data['user'] = u.username
        data['avatar'] = u.avatar
        data['comments_num'] = len(t.comments)
        data['topic_id'] = c.topic_id
        r['data'] = data
        # print('new comment', r)
    else:
        r['success'] = False
        message = c.error_message()
        r['message'] = message
        # print('new topic failure', r)
    return json.dumps(r, ensure_ascii=False)
    # return json.JSONDecoder()



@main.route('/comment/delete/<int:id>', methods=['get'])
def delete(id):
    form = request.form
    print('form', form)
    c = Model.query.get(id)
    c.delete()

    r = {
        'success': True
    }
    return json.dumps(r, ensure_ascii=False)

