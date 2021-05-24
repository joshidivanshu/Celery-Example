## Celery Example Project
### Running on Local Machine
```angular2html
git clone https://github.com/joshidivanshu/Celery-Example
```
```angular2html
pip install -r requirements.txt
```
```angular2html
python manage.py migrate
```
```angular2html
python manage.py runserver
```
### To run celery workers
```angular2html
celery -A mysite worker -l info
```
###To run & install RabbitMQ using Docker
```angular2html
docker run rabbitmq
```