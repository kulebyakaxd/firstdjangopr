from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, CreateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm  


from .models import ToDo,ToDoHistory

# Create your views here.


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'firstapp/index.html', {'todo_list': todos,'title':'Главная страница'})

def history(request):
    todoshist = ToDoHistory.objects.all()
    return render(request, 'firstapp/history.html', {'todo_list': todoshist,'title':'Главная страница'})

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')



def update(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    # todo.is_complete = not todo.is_complete
    if todo.status == "не начато":
        todo.status = "в процессе"
    elif todo.status == "в процессе":
        todo.status = "завершено"
    else:
        todo.status = "не начато"
    todo.save()
    return redirect('index')

def delete(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    addhistory(request,todo_id)
    todo.delete()
    return redirect('index')

def addhistory(request,objid):
    todo = ToDo.objects.get(id=objid)
    todhist = ToDoHistory(title = todo.title, status = todo.status)
    todhist.save()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = RegistrationForm()
    return render(request, 'firstapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')  
            else:
                return render(request, 'firstapp/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()

    return render(request, 'firstapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')  

