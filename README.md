## Установка и запуск:
- Клонировать репозиторий;
```shell
git clone https://github.com/akorsunov23/edtech.git
```
- Создать виртуальное окружение и активировать его;
```shell
python3 -m venv venv
```
- Установить зависимости;
```shell
pip install -r req.txt
```
- Выполнить миграции;
```shell
python manage.py migrate
```
- Загрузить фикстуру;
```shell
python manage.py loaddata db.json
```
- Запустить локальный сервер.
```shell
python manage.py runserver
```

Проект будет доступен по умолчанию на 127.0.0.1:8000

Доступ к админ-панели:
- username: admin
- password: admin


