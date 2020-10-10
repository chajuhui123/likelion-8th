# 장고에 내장되어있는 forms를 불러옴
from django import forms
from .models import FirstModel

# Form 이용해서 하는 법
class Firstform(forms.Form):
    recommend = (
        #저장되는 것은 앞에껏 뒤에는 표시되는 것
        ('GOOD','좋아요'),
        ('BAD','싫어요'),
    )
    title = forms.CharField()
    #forms에는 TextField가 없기 때문에 widget을 사용
    text = forms.CharField(widget= forms.Textarea)
    choice = forms.ChoiceField(choices = recommend)

#model Form 불러와서 사용
class Secondform(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = ['title','text','recommend']