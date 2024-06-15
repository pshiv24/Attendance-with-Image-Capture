from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=True)


class Roster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    working_days = models.CharField(max_length=100)


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="attendance_images/")
