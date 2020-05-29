from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

# chamar o model e do model o django entendeo que pegar do banco de dados

def hello_world(request):
    return HttpResponse('hello');

def task_list(request):
    tasks_list = Task.objects.all().order_by('-created_at')                     # o conteúdo dessa variável vai pro front
    paginator = Paginator(tasks_list, 3)                                         # recebe a lista e nº da página
    page = request.GET.get('page')                                                     # argumento do request automático que vem junto na url
    tasks = paginator.get_page(page)                                                # exibe o numero correto da página na página que ele tá
    return render(request, 'tasks/list.html', {'tasks': tasks});             # no dict: nome da variável no front e valor que ela recebe

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task});

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')                    #redireciona para home

    else:
        form = TaskForm()
        return render(request, 'tasks/addTask.html', {'form': form})

def edit_task(request, id):                         # usar id para achar a TASK
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)                  # instance = deixar o form pré populado e mostrar pro usuário

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance= task)     # UPDATE = pegando dados que vem do POST

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/editTask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/editTask.html', {'form': form, 'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

def your_name(request, name):
    return render(request, 'tasks/yourName.html', {'name': name});

##go back to mother Luzia/s dump