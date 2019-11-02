
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_BanToChuc = models.BooleanField(default=False)
    is_DonViDuThi = models.BooleanField(default=False)

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


    

class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length = 50)
    day_start = models.DateField(auto_now=False)
    day_end = models.DateField(auto_now=False)
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return self.name

    def getDay(self):
        return self.day_start.strftime("%d")
    
    def getMonth(self):
        return self.day_start.strftime("%m")
    
    def getYear(self):
        return self.day_start.strftime("%Y")


class School(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    website = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)

    def __str__(self):
        return(self.name)



class Student(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)


    name = models.CharField(max_length = 50)
    birthday = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    identity_number = models.CharField(max_length = 20)
    phone_numer = models.CharField(max_length = 20)

    STATUS = (
       ('accepted', 'Chấp nhận'),
       ('rejected', 'Từ chối'),
       ('waiting', 'Đang đợi'),
    )
    status = models.CharField(
       max_length=32,
       choices=STATUS,
       default='waiting',
    )


    def __str__(self):
        return self.name
    
    def display_status_value(self):
        return dict(self.STATUS)[self.status]

    
class Contest_Participant(models.Model):
    STATUS = (
       ('accepted', 'Chấp nhận'),
       ('rejected', 'Từ chối'),
       ('waiting', 'Đang đợi'),
    )

    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, null=True)
    participant  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)

    status = models.CharField(
       max_length=32,
       choices=STATUS,
       default='waiting',
    )

    subjects = models.ManyToManyField('Subject')

    def display_status_value(self):
        return dict(self.STATUS)[self.status]



    



    

