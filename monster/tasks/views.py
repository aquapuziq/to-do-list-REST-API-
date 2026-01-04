from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from . import repo
from .validation import TaskSerializer
from .tasks import log_task_created

class TaskList(APIView):
    def get(self, request):
        cached = cache.get("tasks")
        if cached:
            return Response(cached)

        data = repo.get_all()
        cache.set("tasks", data, 60)
        return Response(data)

    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        task = repo.create(serializer.validated_data)

        cache.delete("tasks")

        log_task_created.delay(task["id"])
        return Response(task, status = status.HTTP_201_CREATED)


class TaskDetail(APIView):
    def get(self, request, task_id):
        task = repo.get_one(task_id)
        if not task:
            return Response(status = 404)
        return Response(task)

    def put(self, request, task_id):
        serializer = TaskSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        task = repo.update(task_id, serializer.validated_data)
        return Response(task)

    def patch(self, request, task_id):
        serializer = TaskSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        task = repo.update(task_id, serializer.validated_data)
        return Response(task)

    def delete(self, request, task_id):
        repo.delete(task_id)
        return Response(status = status.HTTP_204_NO_CONTENT)

