from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp" #이렇게 써놓으면 나중에 path 지정할때 좋다.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]