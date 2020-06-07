from django.db import models
from django.conf import settings


class Question(models.Model):
    CHOICES = (
        ("CH1", "Choice 1"),
        ("CH2", "Choice 2"),
        ("CH3", "Choice 3"),
        ("CH4", "Choice 4")
    )
    question = models.CharField(max_length=200)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)
    choice_3 = models.CharField(max_length=100)
    choice_4 = models.CharField(max_length=100)
    marks = models.IntegerField(default=int(5))
    correct_choice = models.CharField(choices=CHOICES, max_length=3)

    def __str__(self):
        return self.question


class TestSet(models.Model):
    TITLE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    questions = models.ManyToManyField(Question)
    title = models.CharField(choices=TITLE, max_length=2)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if int(self.user_id) % 2 != 0:
    #         self.title = 'A'
    #     else:
    #         self.title = 'B'
    #     super(TestSet, self).save(*args, **kwargs)



