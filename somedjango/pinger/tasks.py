import grpc
import os

import timeit
from elasticsearch import Elasticsearch

# from pinger.stubs import ping_pb2
from somedjango import app


from somedjango.settings import PING_STUB
from stubs import ping_pb2, ping_pb2_grpc

es = Elasticsearch()

@app.task()
def start_periodic_task(comment):
    print("Doing ping {}".format(comment))
    response = PING_STUB.Ping(ping_pb2.Request(message="PING"), timeout=1.0)
    print("response")
    print(response)


@app.task()
def start_task_with_task(comment):
    print("Hello kids, i'm going to schedule another task")
    subtask_task.s("0", False).apply_async()


@app.task()
def subtask_task(msg, stap):
    print("I'm that child task :D {} with {}".format(msg, stap))
    if not stap:
        print("and i'm going to schedule another task {}".format(msg))
        for i in range(0, 20):
            sub_subtask_task.s("{}.{}".format(msg, i), stap).apply_async()
    else:
        print("STAHP {}".format(msg))


@app.task()
def sub_subtask_task(msg, stap):
    print("I'm sub sub sub tasky {}".format(msg))
    if not stap:
        print("and i'm going to schedule another sub task sub sub task {} with {}".format(msg, stap))
        response = PING_STUB.Ping(ping_pb2.Request(message="PING"), timeout=1.0)
        print("response for {}".format(msg))
        print(response)
    else:
        print("SAB STAHP {}".format(msg))
