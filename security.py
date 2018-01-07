#from werkzeug.securty import safe_str_cmp
from models.user import UserModel

users = [
    UserModel('bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

#authenticate users
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identify(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
