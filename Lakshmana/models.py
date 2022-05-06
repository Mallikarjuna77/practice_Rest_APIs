from django.db import models

class Dept(models.Model):
    Department=models.CharField(max_length=25)

    def __str__(self):
        return self.Department

class Admin(models.Model):
    Firstname=models.CharField(max_length=25)
    Lastname=models.CharField(max_length=30)
    Emp_Id=models.IntegerField()
    Department=models.ForeignKey(Dept, on_delete=models.CASCADE)
    email=models.EmailField(max_length=40, default=True)
    gender=models.CharField(max_length=12, default=True)
    Address=models.CharField(max_length=100, default=True)

    def __str__(self):
        return self.Firstname


