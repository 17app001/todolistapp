from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


def create(request):
    message = ""
    user = request.user
    form = None
    if not user.is_authenticated:
        message = "請先登入..."
    else:
        if request.method == "POST":
            form = TodoForm()
            print(request.POST)
            # 產生對應的TodoForm跟todo物件
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                # 指定user
                todo.user = request.user
                todo.save()
                message = "建立todo成功!"

    return render(
        request, "./todo/create.html", {"form": form, "message": message, "user": user}
    )


def view(request, id):
    message = ""
    form, todo = None, None
    user = request.user
    try:
        if user.is_authenticated:
            todo = Todo.objects.get(id=id, user=user)
            form = TodoForm(instance=todo)
            if request.method == "POST":
                form = TodoForm(request.POST, instance=todo)
                if form.is_valid():
                    form.save()
                    message = "修改成功!"
                else:
                    message = "修改錯誤!"

        else:
            message = "請先登入..."
    except Exception as e:
        print(e)
        message = "無此代辦事項"

    return render(
        request,
        "./todo/view.html",
        {"todo": todo, "form": form, "message": message},
    )


# Create your views here.
def todo(request):
    user = request.user
    todos = None
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)
        print(todos)

    return render(request, "./todo/todo.html", {"todos": todos})
