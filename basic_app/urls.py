from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'basic_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/', views.PostCreateView.as_view(), name='create_post'),
    path('posts/', views.PostsListView.as_view(), name='posts'),
    re_path(r'^post/(?P<pk>\d+)/delete$', views.PostDeleteView.as_view(), name='delete_post'),
    re_path(r'^post/(?P<pk>\d+)/comment$', views.CommentCreateView.as_view(), name='post_comment'),
    re_path(r'^post/(?P<pk>\d+)/comments$', views.CommentsListView.as_view(), name='comments_list'),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback'),
    re_path(r'^edit-profile/(?P<pk>\d+)/$', views.MyProfileUpdateView.as_view(), name='edit_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name='view_profile'),
]