# YaTubeAPI

Обучающий проект Yatube является прототипом сети для публикации постов,
подписки на интересных авторов и комментирования их 
записей.

Для проекта Yatube реализовано API на основе Django Rest Framework.
Аутентификация осуществляется с помощью токена JWT.

### Установка

Клонируйте репозиторий и перейдите в папку с проектом
```
git clone git@github.com:nepa27/api_final_yatube.git
cd yatube_api
```
Создайте **виртуальное окружение**
```
python3 -m venv venv
source venv/bin/activate    # (Ubuntu)
./venv/Scripts/python       # (Windows)
```
Затем установите необходимые зависимости из файла **requirements.txt**
```
pip install -r requirements.txt
```
Выполните миграции
```
python manage.py runserver
```

## Запуск

Перейдите в корневую директорию проекта, где находится файл **manage.py**
и запустите сервер
```
cd yatube_api
python3 manage.py runserver
```
Если вы все правильно сделали, то высветится приглашение
```
System check identified no issues (0 silenced).
April 20, 2024 - 15:35:58
Django version 3.2.16, using settings 'yatube_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Откройте браузер и перейдите по адресу **http://127.0.0.1:8000/** 

При возникновении ошибки
```
python: can't open file 'yatube_api/manage.py'[Errno 2] No such file or directory
```
убедитесь, что вы находитесь в корневой директории проекта

### Примеры запросов 
* Получение и создание постов: 
  ```
  http://127.0.0.1:8000/api/v1/posts/
  ```
* Получение и создание нового комментария: 
  ```
  http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
  ```
* Получение списка доступных групп: 
  ```
  http://127.0.0.1:8000/api/v1/groups/
  ```
* Получение JWT-токена:
  ```
  http://127.0.0.1:8000/api/v1/jwt/create/
  ```
* Обновление JWT-токена:
  ```
  http://127.0.0.1:8000/api/v1/jwt/refresh/
  ```
* Проверка JWT-токена: 
  ```
  http://127.0.0.1:8000/api/v1/jwt/verify/