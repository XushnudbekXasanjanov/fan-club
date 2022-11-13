from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS = (
        (1, 'manager'),
        (2, 'user'),
    )
    types = models.IntegerField(choices=STATUS, default=2, null=True, blank=True)


class Team(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='team/')
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    missed = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    totalgoal = models.IntegerField(default=0)

    def str(self):
        return self.name


class Turnir(models.Model):
    name = models.CharField(max_length=555)
    date = models.DateField()
    clubs = models.ManyToManyField(Team)

class NextMatch(models.Model):
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE)
    club_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="club_1")
    club_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="club_2")
    date = models.DateTimeField()
    stadium = models.CharField(max_length=255)

class Match(models.Model):
    match = models.ForeignKey(NextMatch, on_delete=models.CASCADE)
    club_1_result = models.IntegerField()
    club_2_result = models.IntegerField()
    club_1_muallif1 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif1 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif2 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif2 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif3 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif3 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif4 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif4 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif5 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif5 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif6 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif6 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif7 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif7 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif8 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif8 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif9 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif9 = models.CharField(max_length=255, null=True, blank=True)
    club_1_muallif10 = models.CharField(max_length=255, null=True, blank=True)
    club_2_muallif10 = models.CharField(max_length=255, null=True, blank=True)


class AllMatchs(models.Model):
    first_team = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="jamoa_1")
    second_team = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="jamoa_2")
    date = models.CharField(max_length=255)
    tur = models.CharField(max_length=255)
    tournament = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255)


class Players(models.Model):
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    img = models.ImageField(upload_to='players/')
    video = models.FileField(upload_to='playervideos/',null=True,blank=True)
    number = models.IntegerField(unique=True)


class CategoryBlogs(models.Model):
    name = models.CharField(max_length=255)

class Blogs(models.Model):
    img = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(CategoryBlogs,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

class Table(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='tablepng/')