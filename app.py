from flask import Flask

from register.controllers import register_bp
from login.controllers import login_bp
from user.controllers import user_bp
from fitness_center.controllers import fitness_center_bp

app = Flask(__name__)

app.register_blueprint(register_bp, url_prefix='/register')
app.register_blueprint(register_bp, url_prefix='/login')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(user_bp, url_prefix='/fitness_center')

if __name__ == '__main__':
    app.run()
