# Django To-Do📝 Web App

A simple to-do web application built using Python Django framework.

## 🚀 Features
- User Registration, Login & Logout
- Task Create, Update & Delete
- Current logged In user can see only their task

## 🗂️ Project Structure
    TO DO WEB APP/
    |--->.venv
    |--->to_do_app
    |   |--->templates
    |   |--->to_do_app
    |   |--->todo_task
    |   |   |--->migrations
    |   |   |--->templates
    |   |       |--->todo_task
    |   |--->users
    |   |   |--->migrations
    |   |   |--->templates
    |   |       |--->users
    |   |--->db.sqlite3
    |   |--->manage.py
    |--->.gitignore
    |--->README.md

## 🛠️ Installation

1. Clone the Repository:
    ```git clone https://github.com/username/django-todo.git```


2. Create a Virtual Environment and activate it:
    ```python -m venv .venv```
    ```.venv\Scripts\activate```


3. Install Dependencies:
    ```pip install -r requirements.txt```

4. Run Migrations and Start the Server:
    ```python manage.py migrate```
    ```python manage.py runserver```

    *💡 Note:* If you want to make any change in *`models.py`*, after making change don't forget to run:
        ```python manage.py makemigrations```
        ```python manage.py migrate```

## 🔗 Useful Links
- [Official Django documentation](https://docs.djangoproject.com/)

## 🙋‍♂️ Author
- Santosh Paudel 
- [Github Profile: Santosh Paudel](https://github.com/oye-san7osh)

