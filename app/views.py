from logging import LogRecord
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from .forms import BookForm , CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

     if request.user.is_authenticated:
          return redirect('/show')
     else:
          form=CreateUserForm()
          if request.method == 'POST':
                    form=CreateUserForm(request.POST)
                    if form.is_valid():
                         form.save()
                         return redirect('/login')
          context = {'form':form}
          return render(request, 'register.html', context)

def loginPage(request):

     if request.user.is_authenticated:
          return redirect('/show')
     else:
          if request.method == 'POST':
               username =  request.POST.get('username')
               password = request.POST.get('password')
          
               user = authenticate(request, username=username, password=password)
               # print(user)
               if user is not None:
                    login(request, user)
                    return redirect('/show')
               else:
                    messages.info(request, 'username or password is incorrect')

          context = {}
          return render(request, 'login.html', context)

def logoutUser(request):
     logout(request)
     return redirect('/login')

def home(request):
     book=Book.objects.all
     # print(book)
     return render(request, 'home.html', {'book': book})
    


def load_form(request):
     form=BookForm
     return render(request, "add.html", {'form':form})

def add(request):
     form=BookForm(request.POST)
     form.save()
     return redirect('/show')

@login_required(login_url='/login')
def showbook(request):
     book=Book.objects.all
     # print(book)
     return render(request, 'show.html', {'book': book})

@login_required(login_url='/login')
def edit(request, id):
     book = Book.objects.get(id=id)
     return render(request, 'edit.html', {'book':book})

@login_required(login_url='/login')
def update(request, id):
     book = Book.objects.get(id=id)
     form = BookForm(request.POST, instance=book)
     if form.is_valid():
          form.save()
     return redirect('/show')


@login_required(login_url='/login')
def delete(request, id):
     book = Book.objects.get(id=id)
     book.delete()
     return redirect('/show')
