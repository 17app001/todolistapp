from django.shortcuts import render, HttpResponse
from todo.models import Todo
from django.contrib.auth.models import User
import json


def todos_user_api(requests, id):
    json_data = {"result": "error", "total": 0, "user": None, "data": []}
    todo_list = []
    try:
        user = User.objects.get(id=id)
        todos = Todo.objects.filter(user=user)
        json_data["total"] = len(todos)
        json_data["user"] = user.username
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
            }
            todo_list.append(data)

        json_data["data"] = todo_list
        json_data["result"] = "success"
    except Exception as e:
        print(e)

    json_data = json.dumps(json_data, ensure_ascii=False)

    return HttpResponse(json_data, content_type="application/json")


def user_api(requests, id):
    data = {"result": "error", "data": {}}
    try:
        user = User.objects.get(id=id)
        data["data"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            "is_superuser": user.is_superuser,
            "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S")
            if user.last_login is not None
            else None,
        }

        data["result"] = "success"
    except Exception as e:
        print(e)

    json_data = json.dumps(data, ensure_ascii=False)

    return HttpResponse(json_data, content_type="application/json")


def users_api(requests):
    users = User.objects.all()
    json_data = {}
    user_list = []
    json_data["total"] = len(users)
    try:
        for user in users:
            data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                "is_superuser": user.is_superuser,
                "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S")
                if user.last_login is not None
                else None,
            }

            user_list.append(data)
    except Exception as e:
        print(e)

    json_data["result"] = user_list
    json_data = json.dumps(json_data, ensure_ascii=False)

    return HttpResponse(json_data, content_type="application/json")


# Create your views here.
def todo_api(requests, id):
    data = {"result": "error", "data": {}}
    try:
        todo = Todo.objects.get(id=id)
        data["data"] = {
            "id": todo.id,
            "title": todo.title,
            "text": todo.text,
            "created": todo.created.strftime("%Y-%m-%d %H:%M:%S"),
            "completed": todo.completed,
            "date_completed": todo.date_completed.strftime("%Y-%m-%d %H:%M:%S")
            if todo.date_completed is not None
            else None,
            "important": todo.important,
            # "image_url": todo.image.url if todo.image is not None else None,
            "user": todo.user.username,
        }
        data["result"] = "success"

    except Exception as e:
        print(e)

    json_data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(json_data, content_type="application/json")


def todos_api(requests):
    todos = Todo.objects.all()
    json_data = {}
    todo_list = []
    json_data["total"] = len(todos)
    try:
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
    except Exception as e:
        print(e)

    json_data["result"] = todo_list
    json_data = json.dumps(json_data, ensure_ascii=False)

    return HttpResponse(json_data, content_type="application/json")
