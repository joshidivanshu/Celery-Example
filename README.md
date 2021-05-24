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
### To run & install RabbitMQ using Docker
```angular2html
docker run rabbitmq
```


### Project Snapshots
![Screenshot from 2021-05-24 15-15-58](https://user-images.githubusercontent.com/32302492/119329605-0684f500-bca3-11eb-81fb-fa7dbe2ea2bd.png)
![Screenshot from 2021-05-24 15-16-03](https://user-images.githubusercontent.com/32302492/119329617-08e74f00-bca3-11eb-9ac2-fd796b01d901.png)
![Screenshot from 2021-05-24 15-16-14](https://user-images.githubusercontent.com/32302492/119329624-0be23f80-bca3-11eb-8bd7-a760e00956fc.png)
