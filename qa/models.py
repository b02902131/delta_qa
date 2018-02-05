from django.db import models

# Create your models here.
class CQA(models.Model):
    pub_date = models.DateTimeField('data published')
    context_text = models.CharField(max_length=1000)
    question_text = models.CharField(max_length=200)
    answer_start = models.IntegerField()
    answer_end = models.IntegerField()
    answer_text = models.CharField(max_length=200)
    valid = models.IntegerField(default=0)
    def __str__(self):
        return "Q: " + self.question_text + ", A: " + self.answer_text
