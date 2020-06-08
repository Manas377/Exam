from django.db import models
from exam.models import Question
from django.core.exceptions import ValidationError


CHOICES = (
    ("C1", "Choice 1"),
    ("C2", "Choice 2"),
    ("C3", "Choice 3"),
    ("C4", "Choice 4")
)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.question.question

    def save(self, *args, **kwargs):
        if self.pk:
            raise ValidationError("you may not edit an existing %s" % self._meta.model_name)
        super (Answer, self).save(*args, **kwargs)


class AnswerSet(models.Model):
    title = models.CharField(max_length=1)
    answer = models.ManyToManyField(Answer)