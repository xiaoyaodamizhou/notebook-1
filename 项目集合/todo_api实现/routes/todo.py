from routes import *
from models.todo import Todo
import json

main = Blueprint('todo', __name__)

@main.route('/')
def index():
    todos = Todo.query.all()
    return render_template('todo.html', todos=todos)

@main.route('/api/todo/add', methods=['post'])
def add():
    data = request.get_data()
    data = data.decode('utf-8')
    # print('response_add', data, type(data))
    form = json.loads(data)
    # print('form_add', form, len(form), type(form))
    # print('error ?', type(Todo))
    t = Todo(form)
    # print('todo_add', t)
    r = {
        'data': {}
    }
    if t is not None:
        t.save()
        data = t.json()
        r['success'] = True
        r['data'] = data
    else:
        r['success'] = False
        r['message'] = 'todo add failure'
    return json.dumps(r, ensure_ascii=False)


@main.route('/api/todo/update', methods=['post'])
def update():
    data = request.get_data()
    data = data.decode('utf-8')
    form = json.loads(data)
    id = form.get('id')
    t = Todo.query.filter_by(id=id).first()
    t.update(form)
    r = {
        'data': {}
    }
    if t is not None:
        td = t
        td.save()
        data = td.json()
        r['success'] = True
        r['data'] = data
    else:
        r['success'] = False
        r['message'] = 'todo update failure'
    return json.dumps(r, ensure_ascii=False)


@main.route('/api/todo/delete', methods=['post'])
def delete():
    data = request.get_data()
    data = data.decode('utf-8')
    form = json.loads(data)
    id = form.get('id')
    t = Todo.query.get(id)
    t.delete(form)
    r = {
        'success': True,
        'id': id
    }
    return json.dumps(r, ensure_ascii=False)

