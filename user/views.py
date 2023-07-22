from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def user_register(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if len(password1) < 8:
            message = "密碼過短"
        elif password1 != password2:
            message = "兩次密碼不相同"
        else:
            if User.objects.filter(username=username):
                message = "帳號已經註冊過"
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                message = "帳號註冊成功!"

        print(username, password1, password2)

    form = UserCreationForm()
    return render(request, "./user/register.html", {"form": form, "message": message})
