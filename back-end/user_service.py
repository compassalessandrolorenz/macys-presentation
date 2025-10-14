import re
import hashlib
import uuid
import random
import string
from datetime import datetime, timedelta, date
from models import db
from models.user import User

# --- Funções de Validação ---

def is_valid_email(email):
    """Valida o formato do email."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_strong_password(password):
    """Valida a força da senha."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def is_valid_zip_code(zip_code):
    """Valida o formato do código postal (5 dígitos)."""
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, zip_code))

def is_over_18(birth_date):
    """Verifica se o usuário tem 18 anos ou mais."""
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age >= 18

def generate_coupon_code():
    """Gera um código de cupom único."""
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"SAVE25-{random_part}"

# --- Funções Auxiliares ---

def hash_password(password):
    """Gera um hash seguro para a senha."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_email_unique(email):
    """Verifica se o email já está cadastrado."""
    return User.query.filter_by(email=email).first() is None

# --- Lógica de Negócio do Usuário ---

def create_user(name, email, password):
    """Cria um novo usuário."""
    if not is_email_unique(email):
        return {'success': False, 'message': 'This email is already registered.'}
    if not is_valid_email(email):
        return {'success': False, 'message': 'Invalid email.'}
    if not is_strong_password(password):
        return {'success': False, 'message': 'Password does not meet minimum security requirements.'}

    token = str(uuid.uuid4())
    token_expiration = datetime.utcnow() + timedelta(days=1)
    
    new_user = User(
        name=name,
        email=email,
        password=hash_password(password),
        activation_token=token,
        token_expiration=token_expiration
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return {
        'success': True,
        'message': 'User created successfully.',
        'user_id': new_user.id,
        'token': token
    }

def send_activation_email(email, token):
    """Simula o envio de um email de ativação."""
    activation_link = f"http://127.0.0.1:8080/activate.html?token={token}"
    print(f"Enviando email de ativação para {email}.")
    print(f"Link: {activation_link}")
    return True

def activate_account(token):
    """Ativa a conta do usuário."""
    user = User.query.filter_by(activation_token=token).first()
    
    if not user:
        return {'success': False, 'message': 'Invalid activation token.'}
        
    if user.token_expiration < datetime.utcnow():
        return {'success': False, 'message': 'Activation token expired.'}

    user.active = True
    user.activation_token = None
    user.token_expiration = None
    db.session.commit()
    
    return {'success': True, 'message': 'Account activated successfully.'}

def authenticate_user(email, password):
    """Authenticates a user."""
    user = User.query.filter_by(email=email).first()
    
    if not user or user.password != hash_password(password):
        return {'success': False, 'message': 'Invalid email or password.'}
    
    if not user.active:
        return {'success': False, 'message': 'Account not activated. Check your email.'}
    
    return {
        'success': True,
        'message': 'Authentication successful.',
        'user': {'id': user.id, 'name': user.name, 'email': user.email}
    }

def subscribe_user(email, zip_code, birth_date):
    """Subscribes a user to the email list."""
    # Busca o usuário pelo email
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return {'success': False, 'message': 'User not found.'}
    
    # Valida o código postal
    if not is_valid_zip_code(zip_code):
        return {'success': False, 'message': 'Invalid zip code. Must be 5 digits.'}
    
    # Converte a string de data para objeto date
    try:
        if isinstance(birth_date, str):
            birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()
        else:
            birth_date_obj = birth_date
    except ValueError:
        return {'success': False, 'message': 'Formato de data inválido. Use YYYY-MM-DD.'}
    
    # Verifica se o usuário tem 18 anos ou mais
    if not is_over_18(birth_date_obj):
        return {'success': False, 'message': 'Você deve ter 18 anos ou mais para se inscrever.'}
    
    # Verifica se o usuário já está inscrito
    if user.subscribed:
        return {'success': False, 'message': 'Este email já está inscrito.'}
    
    # Gera um código de cupom único
    coupon_code = generate_coupon_code()
    
    # Atualiza o registro do usuário
    user.zip_code = zip_code
    user.birth_date = birth_date_obj
    user.subscribed = True
    user.subscription_date = datetime.utcnow()
    user.coupon_code = coupon_code
    
    db.session.commit()
    
    return {
        'success': True,
        'message': 'Inscrição realizada com sucesso!',
        'coupon_code': coupon_code
    }

