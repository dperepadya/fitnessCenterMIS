from flask import Blueprint, jsonify, request
from register import handlers as hndl
from models.user import User

register_bp = Blueprint('register', __name__)


# Get a Registration form
@register_bp.get('/')
def get_registration_form():
    form = """<form action="/register" method="post">
            <label for="name">Name:       </label>
            <input type="text" id="name" name="name" required><br>
            
            <label for="date_of_birth">Date of birth:</label>          
            <input type="date" id="date_of_birth" name="date_of_birth" required><br>  
            
            <label for="address">Address:     </label>
            <input type="text" id="address" name="address" required><br>
            
            <label for="phone">Phone     :     </label>
            <input type="text" id="phone" name="phone" required><br>
            
            <label for="email">e-mail     :     </label>
            <input type="text" id="email" name="email" required><br>
            
            <input type="submit" value="Submit">
            </form>"""
    return form


# Add a user to DB
@register_bp.post('/')
def new_user():
    user_data = request.form
    user = User(user_data['name'], user_data['date_of_birth'], user_data['address'], user_data['phone'],
                user_data['email'])
    result = hndl.insert_to_db(user)
    if result:
        return jsonify({'message': f"New user {user.name}: created successfully"}), 201
    else:
        return jsonify({'message': 'Cannot create new user '}), 400
