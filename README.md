# Шаблон для Aiogram 3

# Features
- Commitizen (проверка стиля коммитов)
- Pre-commit (пре-коммит хуки)
- Ruff (линтер)
- Python Semantic Release (семантическое версионирование)

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

Перед публикацией необходимо указать персональный токен в переменных окружения  
```bash
export GH_TOKEN=
```
Публикация изменений осуществляется с помощью команды:
```bash
semantic-release version 
``` 