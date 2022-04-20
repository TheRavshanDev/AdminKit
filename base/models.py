from django.db import models
from user.models import MainUser

class Tutorial(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.SET_NULL, null=True)
    tutorial_name = models.CharField(max_length=150)
    tutorial_description = models.TextField(max_length=200)
    tutorial_photo = models.ImageField(upload_to='tutorial-photos')

    def __str__(self):
        return self.tutorial_name

    class Meta:
        verbose_name = 'Tutorial'
        verbose_name_plural = 'More Tutorials'

class TutorialMedia(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    tutorial_videos = models.FileField(upload_to='tutorial-videos')

    def __str__(self):
        return self.tutorial.tutorial_name

    class Meta:
        verbose_name = "Tutorial's media file"
        verbose_name_plural = "Tutorials media file"
