from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class GenerateRandomUserView(FormView):
    template_name = 'test.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('user_list')


class UserList(TemplateView):
    def get(self, request):
        users = User.objects.all()
        return render(request,'list.html',{"users": users})


class HomePage(TemplateView):
    def get(self, request):
        users = User.objects.all()
        if len(users) == 0:
            users = None
        return render(request,'home.html',{"users": users})

