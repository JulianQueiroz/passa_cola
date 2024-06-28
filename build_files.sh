#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instalar virtualenv se não estiver instalado
python3 -m pip install --user virtualenv

# Criar um ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar as dependências do projeto
pip install -r requirements.txt

# Converter arquivos estáticos
python3 manage.py collectstatic --noinput

# Aplicar migrações do banco de dados
python3 manage.py migrate
