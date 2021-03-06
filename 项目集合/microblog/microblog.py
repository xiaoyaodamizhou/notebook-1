from app import app, db, cli
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

def server():
    app.run(debug=True)

if __name__ == '__main__':
    server()