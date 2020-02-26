from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bootstrap import Bootstrap

from models import db
from routes.todo import main as routes_todo

app = Flask(__name__)
db_path = 'todo.sqlite'
manager = Manager(app)
bootstrap = Bootstrap(app)

def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'a secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    app.register_blueprint(routes_todo)

def configured_app():
    configure_app()
    return app

# @manager.command
def server():
    app = configured_app()
    config = dict(
        debug=True,
        host='localhost',
        port=3000,
    )
    app.run(**config)

@manager.command
def db_built():
    db.drop_all()
    db.create_all()


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    configure_manager()
    configured_app()
    # manager.run()
    server()
