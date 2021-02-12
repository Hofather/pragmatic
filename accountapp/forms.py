from django.contrib.auth.forms import UserCreationForm

#form을 상속받아서 별도의 form을 생성하여 사용한다.
class AccountUpdateForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super.__init__(*args,**kwargs)
        self.fields['username'].disabled = True
