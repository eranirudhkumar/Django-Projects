from datetime import datetime
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=15)
    email = models.EmailField()
    mob = models.IntegerField()
    upass = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return self.name + " - " + self.email


class Technology(models.Model):
    tech_name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.tech_name


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=25)
    trainer_age = models.IntegerField(max_length=3)
    trainer_contact = models.CharField(max_length=10)
    trainer_address = models.TextField()
    trainer_joining_date = models.DateField(default=datetime.now)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE,
                                   default='Un-Category')

    def __str__(self):
        print(self.technology)
        return self.trainer_name + " - " + str(self.technology)

class Employee(models.Model):
    no      =models.AutoField(primary_key=True)
    name    =models.CharField(max_length=25)
    dob     =models.DateField(default=datetime.now,blank=True)
    address =models.TextField()

    def __str__(self):
        return self.emp_name

    db_table="employee_detail"