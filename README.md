# 🐾 Clínica Vet API

API REST para gerenciamento de clínica veterinária — cadastro de tutores,
animais, veterinários e agendamento de consultas.

## 🚀 Tecnologias
- Python 3 + Django 4.2
- Django REST Framework
- JWT com SimpleJWT
- Documentação automática com drf-spectacular (Swagger)
- Filtros e paginação

## ⚙️ Como rodar localmente
```bash
# clonar o repositório
git clone https://github.com/denis-vetdev/clinica-vet-api
cd clinica-vet-api

# criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# instalar dependências
pip install -r requirements.txt

# configurar variáveis de ambiente
cp .env.example .env
# edite o .env com sua SECRET_KEY

# rodar migrations
python manage.py migrate

# criar superusuário
python manage.py createsuperuser

# iniciar servidor
python manage.py runserver
```

## 📋 Endpoints principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/auth/login/` | Autenticação — retorna JWT |
| POST | `/api/auth/refresh/` | Refresh do token |
| GET/POST | `/api/tutores/` | Listar e cadastrar tutores |
| GET/PUT/DELETE | `/api/tutores/{id}/` | Detalhe do tutor |
| GET/POST | `/api/animais/` | Listar e cadastrar animais |
| GET/PUT/DELETE | `/api/animais/{id}/` | Detalhe do animal |
| GET/POST | `/api/veterinarios/` | Listar e cadastrar veterinários |
| GET/POST | `/api/consultas/` | Listar e agendar consultas |
| GET/PUT/DELETE | `/api/consultas/{id}/` | Detalhe da consulta |

📖 Documentação completa: `http://localhost:8000/api/docs/`

## 👤 Autor
Denis Oliveira — [LinkedIn](https://linkedin.com/in/denis-oliveira-vetdev)