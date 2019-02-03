from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):      # authenticates the user
	user = UserModel.find_by_username(username)
	#user.find_by_username(username=None)
	if user and safe_str_cmp(user.password, password):    # if the pasword given and mapped password are identical, it returns the user
		return user

def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)