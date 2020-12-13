from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  data_nasc = models.DateField(verbose_name=('Data de nascimento'), null=True)
  sex = models.CharField(verbose_name=("Sexo"), max_length=1, null=True)
  photo = models.ImageField(verbose_name=('Avatar'), upload_to='user/avatar', null=True)
  friends = models.ManyToManyField('self', verbose_name=('Amigos'), blank=True)

  def __str__(self):
    return self.user.username

class Record(models.Model):
  title = models.CharField(verbose_name=("Titulo"), max_length=30)
  scope = models.CharField(verbose_name=("Texto"), max_length=500)
  created_at = models.DateTimeField(verbose_name=("Criaçao"), auto_now_add=True)
  deleted_at = models.DateTimeField(verbose_name=("Deletado"), auto_now=False, auto_now_add=False)
  user = models.ForeignKey(Profile, verbose_name=("Author"), on_delete=models.CASCADE)
  votes = models.IntegerField(verbose_name=("Votos"), default=0)
  is_public = models.BooleanField(verbose_name=("É publico?"))