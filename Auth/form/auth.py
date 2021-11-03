from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from Auth.models import User


class UserInfoForm(ModelForm):
    class Meta:
        model = User
        fields = ["password", "is_developer"]

    def __init__(self, user, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        password = self.cleaned_data["password"]
        if not check_password(password, self.user.password):
            raise ValidationError("账号密码错误")

        return self.cleaned_data
