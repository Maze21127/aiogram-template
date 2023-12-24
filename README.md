# Шаблон для Aiogram 3

# Features
- Commitizen (проверка стиля коммитов)
- Pre-commit (пре-коммит хуки)
- Ruff (линтер)
- Python Semantic Release (семантическое версионирование)

## Клонирование из шаблона

Установить copier  
https://copier.readthedocs.io/en/stable/
```bash
pipx install copier
```  

Скопировать шаблон
```bash
copier copy gh:Maze21127/aiogram-template project_name
```

## Dev Environment

1. Установить зависимости
    ```bash
    poetry install --with DEV
    ```
2. Install Hooks
    ```bash
   pre-commit install
   pre-commit install --hook-type commit-msg
   pre-commit install --hook-type pre-push
    ```