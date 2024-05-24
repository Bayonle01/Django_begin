from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counting', views.counting, name='counting'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('root', views.root, name='root')
]
