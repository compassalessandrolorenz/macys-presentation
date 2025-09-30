from flask import Flask
from config import config
from models import db
import user_service

# Create a Flask app with the same configuration as the main app
app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)
db.init_app(app)

# Create and activate a test user
def create_test_user():
    with app.app_context():
        # Create user
        result = user_service.create_user(
            name='Test User',
            email='test@example.com',
            password='Test@123'
        )
        
        if not result['success']:
            print(f"Failed to create user: {result['message']}")
            return
            
        print(f"User created with ID: {result['user_id']}")
        
        # Activate the user's account
        token = result['token']
        activation_result = user_service.activate_account(token)
        
        if activation_result['success']:
            print("User account activated successfully!")
        else:
            print(f"Failed to activate account: {activation_result['message']}")

if __name__ == '__main__':
    create_test_user()