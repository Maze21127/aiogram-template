# Шаблон для Aiogram 3

# Features
- Commitizen (проверка стиля коммитов)
- Pre-commit (пре-коммит хуки)
- Ruff (линтер)
- Python Semantic Release (семантическое версионирование)
- CI/CD github workflow
- Redis
- SQLAlchemy via Alembic

## Клонирование из шаблона

Установить copier  
https://copier.readthedocs.io/en/stable/  
pipx
```bash
pipx install copier
```  
pip
```bash
pip install copier
``` 

Скопировать шаблон
```bash
copier copy gh:Maze21127/aiogram-template project_name
```

## Локальная разработка
Установить зависимости  
```bash
poetry install --with DEV
 ```
Установить git хуки
```bash
poetry run pre-commit install
poetry run pre-commit install --hook-type commit-msg
poetry run pre-commit install --hook-type pre-push
```
Создание коммитов и публикация изменений.

Для проекта используется семантическое версионирование.  

Коммиты должны соответствовать шаблону tag: message  

Публикация изменений осуществляется с помощью команды:
```bash
semantic-release version 
``` 

## Github actions
Добавить в secrets следующие переменные:
- SSH_HOST
- SSH_USER
- SSH_KEY
- BOT_TOKEN
- REDIS_DSN (если есть Redis)
- DB_DSN (если есть SQLAlchemy (PostgreSQL))