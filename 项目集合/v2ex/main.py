from flask import Flask
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from functools import wraps
from models import db

from routes.node import main as node_routes
from routes.todo import main as todo_routes
from routes.user import main as user_routes
from routes.v2ex import main as v2ex_routes
from routes.topic import main as topic_routes
from routes.comment import main as comment_routes

app = Flask(__name__)

manager = Manager(app)
db_path = 'my.sqlite'


def register_routes(app):
    app.register_blueprint(node_routes, url_prefix='/node')
    app.register_blueprint(todo_routes, url_prefix='/todo')
    app.register_blueprint(user_routes, url_prefix='/user')
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(comment_routes, url_prefix='/api')
    app.register_blueprint(v2ex_routes)


def configure_app():
    app.config['SQLALCHEMY_MODIFICATIONS'] = True
    app.secret_key = 'random key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


# @manager.command
def server():
    configured_app()
    print('server run')
    config = dict(
        debug=True,
        host='localhost',
        port=2000,
    )
    app.run(**config)


@manager.command
def db_built():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    configure_manager()
    configure_app()
    # manager.run()
    server()

