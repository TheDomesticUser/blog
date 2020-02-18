from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.ListView.as_view(), name='posts'),
    path('signup/', views.SignUpFormView.as_view(), name='signup'),
    path('login/', views.LoginFormView.as_view(), name='login'),
]