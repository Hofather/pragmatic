from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
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
