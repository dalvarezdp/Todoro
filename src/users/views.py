from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login a un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        return render(request, 'tasks/login.html')

    def post(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """

        context = dict()
        username = request.POST.get("usr")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user is not None:
            # Usuario autenticado
            request.session["default-language"] = "es"
            django_login(request, user)
            url = request.GET.get('next', 'tasks_list') #Permite redirigir a la url desde donde venga el usuario al hacer login
            return redirect(url)
        else:
            # Usuario no autenticado
            context["error"] = "Wrong username or password"
        return render(request, 'tasks/login.html', context)


def logout(request):
    """
    Hace logout de un usuario
    :param request:
    :return:
    """
    django_logout(request)
    return redirect('login')