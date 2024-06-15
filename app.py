import os

from flask import Flask, g

from database.sqlalchemy_utils import engine, Base, Session

from fitness_center.controllers import fitness_center_bp
from login.controllers import login_bp
from logout.controllers import logout_bp
from register.controllers import register_bp
from user.controllers import user_bp

app = Flask(__name__)

app.secret_key = os.urandom(256)
Base.metadata.create_all(engine)


@app.before_request
def before_request():
    g.db = Session()


@app.teardown_request
def teardown_request(exception=None):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


app.register_blueprint(register_bp, url_prefix='/register')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(logout_bp, url_prefix='/logout')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(fitness_center_bp, url_prefix='/fitness_center')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
