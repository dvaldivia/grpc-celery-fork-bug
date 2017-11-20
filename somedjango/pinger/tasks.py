from pinger.stubs import ping_pb2
from somedjango import app
from somedjango.settings import PING_STUB


@app.task()
def start_periodic_task(comment):
    print("Doing ping {}".format(comment))
    response = PING_STUB.Ping(ping_pb2.Request(message="PING"), timeout=1.0)
    print("response")
    print(response)
