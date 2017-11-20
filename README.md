# grpc-celery-fork-bug

Some repo that reproduces the grpc hanging from celery tasks.

Install
=====

Create a virtualenv, activate it and install reqs.

```
virtualenv pyenv
source pyenv/bin/activate
pip install -r requirements.txt
```

Start the grpc server

```
cd grpc-server/
python serve.py
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
