from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, FormView,
                                    DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from django.urls import reverse
from django.shortcuts import redirect

from . import forms
from . import models

# Temporary
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class PostsDetailView(DetailView):
    model = models.Post

    template_name = 'basic_app/info/user/detail/index.html'

class SignUpCreateView(CreateView):    
    template_name = 'basic_app/signup/index.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        # hash the password. Argon2 by default
        form.instance.password = make_password(form.cleaned_data['password'])

        form.save()

        return render(self.request, self.template_name, context={
            'form': form,
            'signup_success': True
        })

class UserLoginView(LoginView):
    template_name = 'basic_app/login/index.html'

class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'basic_app/index.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'basic_app/create/post/index.html'
    login_url = '../../login/index.html'

    form_class = forms.CreatePostForm

    def form_valid(self, form):
        # set the author of the post
        form.instance.author = self.request.user

        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('basic_app:posts')

class PostsListView(ListView):
    template_name = 'basic_app/info/user/list/posts/index.html'

    model = models.Post
    object_list = 'posts_list'

    ordering = ['-datetime_posted']

class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'basic_app/create/comment/index.html'

    model = models.Comment
    fields = ('comment',)

    def form_valid(self, form, *args, **kwargs):
        # set the post that the user commented on
        post_commented = models.Post.objects.filter(pk=self.kwargs['pk']).first()
        post_commented.save()

        form.instance.post_commented = post_commented

        # set the current user instance as the commenter
        form.instance.commenter = self.request.user

        return super(CommentCreateView, self).form_valid(form)

class CommentsListView(ListView):
    template_name = 'basic_app/info/user/list/comments/index.html'

    model = models.Comment
    object_list = 'comments_list'

    ordering = ['-datetime_commented']

class FeedbackCreateView(CreateView):
    template_name = 'basic_app/create/feedback/index.html'

    form_class = forms.FeedbackForm

    def form_valid(self, form):
        form.save()

        return render(self.request, self.template_name, context={
            'form': form,
            'valid_feedback': True
        })

class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'basic_app/update_profile/index.html'

    model = models.User
    fields = ('profile_pic', 'desc')

class UserProfileDetailView(DetailView):
    template_name = 'basic_app/info/user/detail/index.html'

    model = models.User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context