import os
from flask import Flask, render_template
from database import database
from fitness_center.controllers import fitness_center_bp
from login.controllers import login_bp
from logout.controllers import logout_bp
from register.controllers import register_bp
from user.controllers import user_bp
from utils.login_decorator import user_is_logged_in

app = Flask(__name__)

app.secret_key = os.urandom(256)

app.register_blueprint(register_bp, url_prefix='/register')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(logout_bp, url_prefix='/logout')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(fitness_center_bp, url_prefix='/fitness_center')


database.init_db()



@app.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.close()


@app.get('/')
def landing():
    return render_template('landing.html', user_is_logged_in=user_is_logged_in())


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=5000)
