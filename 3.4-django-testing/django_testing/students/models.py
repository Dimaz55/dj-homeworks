from django.core.exceptions import ValidationError
from django.db import models

from django_testing import settings


class Student(models.Model):
    name = models.TextField()
    birth_date = models.DateField(
        null=True,
    )

    def save(self):
        if Student.objects.count() > 20:
            raise ValidationError(
                f"Max students {settings.MAX_STUDENTS_PER_COURSE}")


class Course(models.Model):
    name = models.TextField()
    students = models.ManyToManyField(
        Student,
        blank=True
    )
