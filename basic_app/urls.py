from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'basic_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('posts/', views.PostsListView.as_view(), name='posts'),
    path('post/', views.PostCreateView.as_view(), name='create_post'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback'),
]