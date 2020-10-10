from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm): # 만들어진 모델로부터 폼을 사용
    class Meta:
        model = Jasoseol
        fields = ('title','body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['body'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title',
            'placeholder':'제목',
        })


        