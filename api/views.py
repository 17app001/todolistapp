from django.shortcuts import render, HttpResponse
from todo.models import Todo
import json
from datetime import datetime


# Create your views here.
# json
def todos_api(requests):
    todos = Todo.objects.all()

    todo_list = []
    for todo in todos:
        data = {
            "id": todo.id,
            "title": todo.title,
            "text": todo.text,
            "created": todo.created.strftime("%Y-%m-%d %H:%M:%S"),
            "completed": todo.completed,
            "date_completed": todo.date_completed.strftime("%Y-%m-%d %H:%M:%S")
            if todo.date_completed is not None
            else None,
            "important": todo.important,
            "user": todo.user.username,
        }

        todo_list.append(data)

    json_data = json.dumps(todo_list, ensure_ascii=False)

    return HttpResponse(json_data, content_type="application/json")
