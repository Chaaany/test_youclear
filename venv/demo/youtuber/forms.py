from django import forms
from .models import *

# 회원가입 폼 커스텀 한 내용 출력 ModelForm 상속 / settings.py에 커스텀 폼 쓴다고 명시
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        # form에 기입된 데이터는 cleaned_data로 가지고 올 수 있음
        user.nickname = self.cleaned_data["nickname"]
        user.save()