from django.db import models
from django.urls import reverse

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50, default='BSIT')
    year = models.PositiveSmallIntegerField(default=1)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['last_name','first_name']

    def __str__(self):
        return f"{self.student_id} - {self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse('students:detail', args=[str(self.id)])
