from django.shortcuts import render, redirect
from django.contrib import messages, auth
from users.models import user

def startpage(request):
    return render(request, 'users/startpage.html')

def logout(request):
    return render(request, 'users/logout.html')

def login(request):
    # return render(request, 'users/login.html')

    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']

        print(login, password)
        print()
        user = auth.authenticate(login = login, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('game/main_lobby.html', {'exist_user':user})
        else:
            messages.info(request, 'Неверный логин или пароль')
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

def register(request):

    if request.method == 'POST':
        # check
        # email = request.POST['email']
        # login = request.POST['login']
        # if user.objects.filter(email = email).exists:
        #     messages.info(request, 'такой емейл есть')
        #     return render(request, 'users/register.html')
        # elif user.objects.filter(login = login).exists:
        #     messages.info(request, 'такой логин есть')
        #     return render(request, 'users/register.html')

        if request.POST.get('email') and request.POST.get('login') and request.POST.get('password'):
            new_user = user()
            new_user.email = request.POST.get('email')
            new_user.login = request.POST.get('login')
            new_user.password = request.POST.get('password')
            new_user.save()
            # print(new_user)
            # messages.success(request, f'пользователь с логином {new_user.login} создан')
            return render(request, 'game/main_lobby.html', {'exist_user':new_user})
    else:
        return render(request,'users/register.html')

# def register(response):

#     if response.method == 'post':
#         user_login = user(login = login)


