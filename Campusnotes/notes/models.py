from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField(blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes/')
    upload_date = models.DateTimeField(default=timezone.now)
    download_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

