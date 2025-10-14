from flask import Flask, request, jsonify
from flask_cors import CORS
from config import config
from models import db
import user_service  # Usaremos o serviço de usuário refatorado

def create_app(config_name='default'):
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    
    # Habilita CORS para permitir requisições do front-end
    CORS(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})
    
    @app.route('/api/register', methods=['POST'])
    def register():
        """Endpoint para registro de novos usuários."""
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Dados não fornecidos.'}), 400

        # Validações básicas
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return jsonify({'success': False, 'message': 'Todos os campos são obrigatórios.'}), 400

        # Cria o usuário usando o serviço
        result = user_service.create_user(name, email, password)

        if not result['success']:
            return jsonify(result), 400
        
        # Simula envio de email com o token
        user_service.send_activation_email(email, result['token'])
        
        return jsonify({
            'success': True,
            'message': 'Cadastro realizado com sucesso! Verifique seu email para ativar sua conta.'
        }), 201

    @app.route('/api/activate/<token>', methods=['GET'])
    def activate(token):
        """Endpoint para ativação da conta."""
        result = user_service.activate_account(token)
        
        if not result['success']:
            # Em uma API, redirecionamentos não são ideais.
            # O front-end decidirá o que fazer com a resposta.
            return jsonify(result), 400
        
        return jsonify(result), 200

    @app.route('/api/login', methods=['POST'])
    def login():
        """Endpoint para autenticação de usuários."""
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Dados não fornecidos.'}), 400

        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'success': False, 'message': 'Email e senha são obrigatórios.'}), 400
        
        result = user_service.authenticate_user(email, password)
        
        if not result['success']:
            return jsonify(result), 401  # Unauthorized
            
        return jsonify(result), 200

    @app.route('/api/subscribe', methods=['POST'])
    def subscribe():
        """Endpoint para inscrição na lista de emails."""
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Dados não fornecidos.'}), 400

        email = data.get('email')
        zip_code = data.get('zipCode')
        birth_date = data.get('birthDate')

        if not all([email, zip_code, birth_date]):
            return jsonify({'success': False, 'message': 'Todos os campos são obrigatórios.'}), 400
        
        result = user_service.subscribe_user(email, zip_code, birth_date)
        
        if not result['success']:
            return jsonify(result), 400
            
        return jsonify(result), 200

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=app.config['DEBUG'])


