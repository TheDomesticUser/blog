from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, FormView,
                                    DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from . import forms
from . import models

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

        # hash the password
        user.password = make_password(user.password)

        # save the user into the database
        user.save()

        return render(self.request, self.template_name, context={ 'signup_success': True, 'form': form })

class LoginFormView(View):
    def get(self, request):
        return render(request, 'basic_app/login.html', context={ 'form': forms.LoginForm })
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = models.User.objects.filter(username=username).first()

        # If user is valid
        if user:
            if check_password(password, user.password):
                print('success')
                return HttpResponse('<h1>Success</h1>')
        
        return HttpResponse('<h1>Failed</h1>')