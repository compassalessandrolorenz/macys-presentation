# Ai Markethub - Sistema de Cadastro de Usuários

Este projeto implementa um sistema de cadastro de usuários para o marketplace Ai Markethub, com validações no front-end e back-end.

## Funcionalidades

- Formulário de cadastro com validações em tempo real
- Validação de formato de email
- Verificação de força da senha (comprimento mínimo, caracteres especiais, letras maiúsculas/minúsculas)
- Confirmação de senha
- Simulação de envio de email de confirmação
- Processo de ativação de conta via token

## Estrutura do Projeto

```
ai-markethub/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── validation.js
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── confirmation.html
│   └── activation.html
│
├── app.py
├── user_service.py
└── README.md
```

## Tecnologias Utilizadas

- **Front-end**: HTML, CSS, JavaScript, Bootstrap
- **Back-end**: Python com Flask
- **Armazenamento**: Simulação em memória (dicionários Python)

## Requisitos

- Python 3.6+
- Flask

## Como Executar

1. Instale as dependências:
```
pip install flask
```

2. Execute a aplicação:
```
python app.py
```

3. Acesse a aplicação no navegador:
```
http://localhost:5000
```

## Fluxo de Cadastro

1. Usuário acessa a página de cadastro
2. Preenche o formulário com nome, email e senha
3. O sistema valida os dados em tempo real
4. Ao enviar o formulário, o sistema valida novamente os dados no servidor
5. Se válido, o usuário é cadastrado e recebe um email de confirmação
6. O usuário clica no link de ativação recebido por email
7. A conta é ativada e o usuário é redirecionado para a página de sucesso

## Casos de Teste

### 1. Cadastro de usuário com sucesso

- **Dado que** o usuário acessa a página de cadastro do Ai Markethub
- **Quando** o usuário preenche corretamente o formulário com nome, e-mail e senha válidos
- **E** o usuário confirma a senha no campo "Confirme"
- **E** o usuário clica em "Validar Cadastro"
- **Então** o sistema deve criar a conta do usuário
- **E** o sistema deve enviar um e-mail de confirmação com link de ativação
- **E** o usuário deve ser redirecionado para uma página de confirmação de cadastro

### 2. Tentativa de cadastro com e-mail já existente

- **Dado que** o usuário acessa a página de cadastro do Ai Markethub
- **Quando** o usuário preenche o formulário com um e-mail já cadastrado no sistema
- **E** o usuário preenche os demais campos corretamente
- **E** o usuário clica em "Validar Cadastro"
- **Então** o sistema deve exibir uma mensagem informando que o e-mail já está em uso
- **E** o sistema não deve criar uma nova conta
- **E** o usuário deve permanecer na página de cadastro

### 3. Tentativa de cadastro com senha fraca

- **Dado que** o usuário acessa a página de cadastro do Ai Markethub
- **Quando** o usuário preenche o formulário com nome e e-mail válidos
- **E** o usuário insere uma senha que não atende aos requisitos mínimos de segurança
- **E** o usuário confirma a senha fraca no campo "Confirme"
- **E** o usuário clica em "Validar Cadastro"
- **Então** o sistema deve exibir uma mensagem de erro sobre a senha fraca
- **E** o sistema deve fornecer orientações sobre os requisitos mínimos de segurança da senha
- **E** o sistema não deve criar uma nova conta
- **E** o usuário deve permanecer na página de cadastro
