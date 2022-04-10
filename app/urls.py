from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('load_form', views.load_form ),
    path('add', views.add ),
    path('show', views.showbook ),
    path('edit/<int:id>', views.edit ),
    path('update/<int:id>', views.update ),
    path('delete/<int:id>', views.delete ),
    path('register', views.register ),
    path('login', views.loginPage ),
    path('logout', views.logoutUser ),

]
