from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #유저관련 form은 주로 contrib 안에 있음
from django.contrib.auth.views import LoginView

def signup(request):
    regi_form = UserCreationForm() #유저생성 폼
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_vaild(): #유효성검사
            filled_form.save() #유저정보 저장
            return redirect('index')
    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView):
    template_name = 'login.html'