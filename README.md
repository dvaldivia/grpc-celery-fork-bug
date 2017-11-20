# grpc-celery-fork-bug

Some repo that reproduces the grpc hanging from celery tasks.

Install
=====

install reqs

```
pip install -r requirements.txt
```

Perform all the following steps in different terminals with the same environment

Start the grpc server

```
cd grpc-server/
python serve.py
```


Start a rabbitmq as broker

```
docker run -it -d -p 5672:5672 -p 15672:15672 rabbitmq
```


Start the celery server

```
cd somedjango/
celery -A somedjango worker -l info
```

Start django to get some tasks scheduled

```
./manage.py runserver
```
