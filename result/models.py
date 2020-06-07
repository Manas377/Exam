from django.db import models
from exam.models import Question


CHOICES = (
    ("C1", "Choice 1"),
    ("C2", "Choice 2"),
    ("C3", "Choice 3"),
    ("C4", "Choice 4")
)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered = models.CharField(max_length=3, null=True, blank=True)


class AnswerSet(models.Model):
    title = models.CharField(max_length=1)
    answer = models.ManyToManyField(Answer)