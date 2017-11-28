# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# class meh(ViewSet):
#
#     def lol(self):
#         return Response({"X": "Y"})
from django.http import HttpResponse

from pinger import tasks


# Create your views here.


def my_view(request):
    # ...

    # Return a "created" (201) response code.
    tasks.start_task_with_task.s("yey").apply_async()

    return HttpResponse(status=200)
