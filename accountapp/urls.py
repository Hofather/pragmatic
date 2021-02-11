from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp" #이렇게 써놓으면 나중에 path 지정할때 좋다.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'), #class 형의 view인 경우에는 as_view()메소드 사용.
]