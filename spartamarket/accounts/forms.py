from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth   import get_user_model
from django.urls import reverse

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model =  get_user_model()      # user를 직접 참조 하는거보단 겟 유저모델을 참조하는게 좋다. 장고는 멀티 유저를 지원하므로 확장성에 용이.
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text
        