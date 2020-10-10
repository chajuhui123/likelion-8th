from django.db import models

# Create your models here.
class Question(models.Model):
    objects = models.Manager()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    # 커스텀 메소드
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    objects = models.Manager()
    question = models.ForeignKey(Question, on_delete = models.CASCADE) #CASCADE는 questions이 삭제되면 choice에 있는 관련 데이터도 삭제되도록 함
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text