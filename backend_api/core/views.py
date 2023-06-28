from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import Todo
from .serializers import TodoSerializer


def home(request):
    return render(request, 'home.html')


# сериалайзер помогает подготавливать и передавать данные в нужном формате по api
@api_view(['GET', 'POST']) # здесь определяем каким методы будет использлвать
def todos_list(request):

    if request.method == 'GET':
        todos = Todo.objects.all()
        # передаем данные для сериализации в сериалайзер, даем знать, что обьектов будет много (many)
        serializer = TodoSerializer(todos, many=True)
        # возвращаем обработанные данные
        return Response(serializer.data)

    if request.method == 'POST':
        name = request.data.get('name')
        todo = Todo.objects.create(name=name)
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data)

