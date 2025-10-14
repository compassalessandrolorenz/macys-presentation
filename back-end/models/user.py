from . import db
from datetime import datetime
import uuid

class User(db.Model):
    """Modelo de dados para o Usuário."""
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    activation_token = db.Column(db.String(36), unique=True, nullable=True)
    token_expiration = db.Column(db.DateTime, nullable=True)
    
    # Subscription fields
    zip_code = db.Column(db.String(5), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    subscribed = db.Column(db.Boolean, default=False, nullable=False)
    subscription_date = db.Column(db.DateTime, nullable=True)
    coupon_code = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'


