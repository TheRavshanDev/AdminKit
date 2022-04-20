from django.db import models
from django.contrib.auth.models import User

class MainUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_address = models.CharField(max_length=110)
    live_address = models.CharField(max_length=110)
    work = models.CharField(max_length=100)
    about = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Main User'
        verbose_name_plural = 'Users'

class IT(models.Model):
    it = models.CharField(max_length=100)

    def __str__(self):
        return self.it

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"

class Skill(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    yonalish = models.ForeignKey(IT, on_delete=models.SET_NULL, null=True)
    skills = models.CharField(max_length=400)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills' 