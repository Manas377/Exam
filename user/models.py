from django.db import models
from exam.models import TestSet


from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll_number = models.IntegerField(default=1)
    test_set = models.ForeignKey(TestSet, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):

        #  this means model IS NOT SAVED to database yet
        if self._state.adding:
            last_roll_number = Student.objects.all().aggregate(largest=models.Max('roll_number'))['largest']

            #  aggregate can also return none, we would need to check it IF IT"S THE FIRST ENTRY.
            #  then we can simply add one to 'last_roll_number' which definitely is the largest roll number.
            if last_roll_number is not None:
                self.roll_number = last_roll_number + 1
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.roll_number