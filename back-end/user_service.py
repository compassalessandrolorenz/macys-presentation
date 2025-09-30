import re
import hashlib
import uuid
from datetime import datetime, timedelta
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
        return {'success': False, 'message': 'Este email já está cadastrado.'}
    if not is_valid_email(email):
        return {'success': False, 'message': 'Email inválido.'}
    if not is_strong_password(password):
        return {'success': False, 'message': 'Senha não atende aos requisitos mínimos de segurança.'}
    
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
        'message': 'Usuário criado com sucesso.',
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
        return {'success': False, 'message': 'Token de ativação inválido.'}
        
    if user.token_expiration < datetime.utcnow():
        return {'success': False, 'message': 'Token de ativação expirado.'}
    
    user.active = True
    user.activation_token = None
    user.token_expiration = None
    db.session.commit()
    
    return {'success': True, 'message': 'Conta ativada com sucesso.'}

def authenticate_user(email, password):
    """Autentica um usuário."""
    user = User.query.filter_by(email=email).first()
    
    if not user or user.password != hash_password(password):
        return {'success': False, 'message': 'Email ou senha incorretos.'}
    
    if not user.active:
        return {'success': False, 'message': 'Conta não ativada. Verifique seu email.'}
    
    return {
        'success': True,
        'message': 'Autenticação bem-sucedida.',
        'user': {'id': user.id, 'name': user.name, 'email': user.email}
    }

