from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, FormView,
                                    DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from . import forms
from . import models

# Python modules
import datetime

# Temporary
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class PostsListView(ListView):
    context_object_name = 'posts_list'
    model = models.Post

    template_name = 'basic_app/posts.html'

class PostsDetailView(DetailView):
    model = models.Post

    template_name = 'basic_app/posts.html'

class SignUpFormView(CreateView):    
    template_name = 'basic_app/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)

        # hash the password. Argon2 by default
        user.password = make_password(user.password)

        # save the user into the database
        user.save()

        return render(self.request, self.template_name, context={ 'signup_success': True, 'form': form })

class UserLoginView(LoginView):
    template_name = 'basic_app/login.html'

@login_required
class UserLogoutView(LogoutView):
    template_name = 'basic_app/base.html'

class PostsListView(ListView):
    template_name = 'basic_app/posts_list.html'

    model = models.Post
    object_list = 'posts_list'

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'basic_app/create_post.html'
    login_url = '../../login/'

    model = models.Post
    
    fields = ('title', 'content')

    def form_valid(self, form):
        data = form.cleaned_data

        post = models.Post(author=self.request.user,
            title=data['title'],
            content=data['content'])

        post.save()

        return render(self.request, 'basic_app/posts_list.html')