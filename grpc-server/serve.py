"""
Copyright (C) 2017 Espressive Inc

"""
import time

import grpc
from concurrent import futures

from stubs import ping_pb2_grpc, ping_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class PingServiceServicer(ping_pb2_grpc.PingServiceServicer):
    def Ping(self, request, context):
        print("serve ping")
        return ping_pb2.Pong(response="pong")


def serve():
    print("Starting grpc server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ping_pb2_grpc.add_PingServiceServicer_to_server(
        PingServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
