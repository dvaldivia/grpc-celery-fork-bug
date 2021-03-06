# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

from pinger import tasks
from somedjango.settings import PING_STUB
from stubs import ping_pb2


class PingerConfig(AppConfig):
    name = 'pinger'

    def ready(self):
        print("Pinger ready")

        response = PING_STUB.Ping(ping_pb2.Request(message="PING"))
        print(response)

        # tasks.start_periodic_task.s("world").apply_async(countdown=2)
        # tasks.start_periodic_task.s("world").apply_async(countdown=4)
        # tasks.start_periodic_task.s("world").apply_async(countdown=6)
        # tasks.start_periodic_task.s("world").apply_async(countdown=8)
        # tasks.start_periodic_task.s("world").apply_async(countdown=10)
        # tasks.start_periodic_task.s("world").apply_async(countdown=12)

        tasks.start_task_with_task.s("Sup").apply_async()
