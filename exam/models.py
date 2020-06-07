from django.db import models
from django.conf import settings


class Question(models.Model):
    CHOICES = (
        ("C1", "Choice 1"),
        ("C2", "Choice 2"),
        ("C3", "Choice 3"),
        ("C4", "Choice 4")
    )
    question = models.CharField(max_length=200)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)
    choice_3 = models.CharField(max_length=100)
    choice_4 = models.CharField(max_length=100)
    marks = models.IntegerField(default=int(5))
    correct_choice = models.CharField(choices=CHOICES, max_length=2)

    def __str__(self):
        return self.question

    def check_answer(self, choice):
        if choice == self.correct_choice:
            return True


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



