from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.question_text

class Context(models.Model):
    context_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.context_text[:100]

class Answer(models.Model):
    answer_start = models.IntegerField()
    answer_end = models.IntegerField()
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return str(self.answer_start) + ", " + str(self.answer_end) + ": " + answer_text
