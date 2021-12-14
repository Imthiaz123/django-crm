from django.db import models
import uuid


class Users(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)


class Employee(models.Model):

    STATES = (
        ("1", "Andhra Pradesh"),
        ("2", "Arunachal Pradesh"),
        ("3", "Assam"),
        ("4", "Bihar"),
        ("5", "Chhattisgarh"),
        ("6", "Goa"),
        ("7", "Gujarat"),
        ("8", "Haryana"),
        ("9", "Himachal Pradesh"),
        ("10", "Jharkhand"),
        ("11", "Karnataka"),
        ("12", "Kerala"),
        ("13", "Madhya Pradesh"),
        ("14", "Maharashtra"),
        ("15", "Manipur"),
        ("16", "Meghalaya"),
        ("17", "Mizoram"),
        ("18", "Nagaland"),
        ("19", "Odisha"),
        ("20", "Punjab"),
        ("21", "Rajasthan"),
        ("22", "Sikkim"),
        ("23", "Tamil Nadu"),
        ("24", "Telangana"),
        ("25", "Tripura"),
        ("26", "Uttar Pradesh"),
        ("27", "Uttarakhand"),
        ("28", "West Bengal"),
    )

    emp_no = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATES, max_length=100)
    pin = models.CharField(max_length=50)
