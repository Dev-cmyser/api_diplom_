from django.db import models
from django.contrib.auth.models import  AbstractUser




class App(models.Model):
    name = models.CharField(max_length=255)
    seconds = models.IntegerField(verbose_name='Время в секундах',blank=True) 
    def __str__(self) -> str:
        return f'{self.name}'



class Task(models.Model):
    apps = models.ManyToManyField(App, related_name='app' )
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
 
    def __str__(self) -> str:
        return f'{self.name}'

class User(AbstractUser):
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)

    USERNAME_FILD = 'username'




def get_name_file(s):
    pass

