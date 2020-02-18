from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


# Create your views here.

class TaskListAPIView(APIView):
    """
    List all tasks
    """

    def get(self, request, format=None):
        """
        Get list of all tasks
        :param request:
        :param format:
        :return:
        """
        tasks = Task.objects.all().order_by("-last_updated_on")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create new task
        :param request:
        :param format:
        :return:
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get_object(self, pk):
        """
        Get an object given its primary key
        :param pk:
        :return:
        """
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Edit an existing task
        :param request:
        :param pk: The primary key
        :param format:
        :return:
        """
        task = self.get_object(pk)
        serializer = TaskSerializer(task, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a task by primary key
        :param request:
        :param pk:
        :param format:
        :return:
        """
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
