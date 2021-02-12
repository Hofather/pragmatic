from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST" :
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return redirect('accountapp:hello_world')
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list':hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class일 때는 lazy를 쓴다. def일 경우 reverse 사용.
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'