from flask import Flask

from register.routes import register_bp
from login.routes import login_bp
from user.routes import user_bp
from fitness_center.routes import fitness_center_bp

app = Flask(__name__)

app.register_blueprint(register_bp, url_prefix='/register')
app.register_blueprint(register_bp, url_prefix='/login')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(user_bp, url_prefix='/fitness_center')

if __name__ == '__main__':
    app.run()
