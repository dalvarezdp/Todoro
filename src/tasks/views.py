from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

from tasks.models import Task


@login_required()
def tasks_list(request):
    """
    Recupera todas las tareas de la base de datos y las pinta
    :param request: HttpRequest
    :return: HttpResponse
    """

    # recuperar todas las tareas de la base de datos
    tasks = Task.objects.select_related("owner", "assignee").all()

    # comprobamos si debe filtrar por tareas creadas por el usuario
    if request.GET.get('filter') == 'owned':
        tasks = tasks.filter(owner=request.user)

    # comprobamos si debe filtrar por tareas asignadas al usuario
    if request.GET.get('filter') == 'assigned':
        tasks = tasks.filter(assignee=request.user)

    # devolver la respuesta
    context = {
        'task_objects': tasks
    }
    return render(request, 'tasks/list.html', context)


def tasks_detail(request, task_pk):
    """
    Recupera una tareaa de la base de datos y las pinta con una plantilla
    :param request: HttpRequest
    :param task_pk: Primary key de la tarea a recuperar
    :return: HttpResponse
    """
    # recuperar la tarea de la base de datos
    try:
        task = Task.objects.select_related().get(pk=task_pk)
    except Task.DoesNotExist:
        #return HttpResponseNotFound("La tarea que buscas no existe.")
        return render(request, 'tasks/404.html', {}, status=404)
    except Task.MultipleObjectsReturned:
        return HttpResponse("Existen varias tareas con ese identificador", status=300)

    # preparar el contexto
    context = {
        'task': task
    }

    # renderizar el contexto
    return render(request, 'tasks/detail.html', context)


def login(request):
    """
    Hace login de un usuario
    :param request: HttpRequest
    :return: HttpResponse
    """

    return render(request, 'tasks/login.html')