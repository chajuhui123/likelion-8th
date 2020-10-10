from django.urls import path, include
from . import views

#class를 함수화 해야합니다
app_name = "cbv"
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>', views.DetailVeiw.as_view(), name = 'detail'),
    path('<int:pk>/results/',  views.ResultsVeiw.as_view(), name="results"),
    path('<int:question_id>/vote/',  views.vote, name="vote"),
]
