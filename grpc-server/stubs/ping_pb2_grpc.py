# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ping_pb2 as ping__pb2


class PingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/bugs.PingService/Ping',
        request_serializer=ping__pb2.Request.SerializeToString,
        response_deserializer=ping__pb2.Pong.FromString,
        )


class PingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=ping__pb2.Request.FromString,
          response_serializer=ping__pb2.Pong.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bugs.PingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
