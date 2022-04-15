# Серверная часть проекта Django Vue SPA 

Серверная часть проекта реализована с использованием [Django Rest Framework](https://www.django-rest-framework.org/) и [PostgreSQL](https://www.postgresql.org/)

## Установка и использование
1. Необходимо скачать проект  
2. Создать и активировать виртуальное окружение  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Установить рекомендуемые библиотеки  
  ```pip install -r requirements.txt```
4. Запустить миграции базы данных и запустить проект  
  ```python manage.py migrate```  
  ```python manage.py runserver```  
