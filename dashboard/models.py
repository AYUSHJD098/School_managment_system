from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=124),
    father_name = models.CharField(max_length=124),
    mother_name = models.CharField(max_length=124),
    address = models.TextField()
    phone = models.IntegerField(),
    phone2 = models.IntegerField(null=True),
    birthdate = models.DateField(),
    standard = models.CharField(max_length=124, choices=(
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
    )),
    student_photo = models.ImageField(null=True, blank=True, upload_to="images/human/"),
    addhar_card = models.ImageField(null=True, blank=True, upload_to="images/addhar/"),
