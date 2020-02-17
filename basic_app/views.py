from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, FormView,
                                    DetailView, CreateView, UpdateView, DeleteView)
from . import forms
from django.urls import reverse
from . import models
from django.contrib.auth.hashers import make_password

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class PostsListView(ListView):
    context_object_name = 'posts_list'
    model = models.Post

    template_name = 'basic_app/posts.html'

class PostsDetailView(DetailView):
    model = models.Post

    template_name = 'basic_app/posts.html'

class SignUpFormView(FormView):    
    template_name = 'basic_app/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)

        # hash the password
        user.password = make_password(user.password)

        # save the user into the database
        user.save()

        return render(self.request, self.template_name, context={ 'signup_success': True, 'form': form })