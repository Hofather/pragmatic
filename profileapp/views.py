from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    #profile의 User가 누군지를 알아야 한다.
    def form_valid(self, form):
        temp_profile = form.save(commit=False) #임시저장
        temp_profile.user = self.request.user #사용자를 넣어주고.
        temp_profile.save() # 저장.

        return super().form_valid(form)