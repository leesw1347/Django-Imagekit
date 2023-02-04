from typing import Tuple

from django.db import models

# Create your models here.

OPTIONS = (
    ('telco' , 'Telecommunication') ,
    ('log' , 'Logistics') ,
    ('agr' , 'Agriculture') ,
    ('aero' , 'Aerospace') ,
    ('pharm' , 'Pharmaceutical') ,
)


class Company(models.Model):
    name = models.CharField(max_length=255 ,
                            help_text='회사명')
    company_type = models.CharField(max_length=15 , choices=OPTIONS , help_text='회사타입')
    founded = models.DateField(null=True , blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


# Django Documentation Example
class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES: Tuple[str , str] = [
        (FRESHMAN , "Freshman") ,
        (SOPHOMORE , "Sophomore") ,
        (JUNIOR , "Junior") ,
        (SENIOR , "Senior") ,
        (GRADUATE , "Graduate")
    ]

    year_in_school = models.CharField(
        max_length=2 ,
        choices=YEAR_IN_SCHOOL_CHOICES ,
        default=FRESHMAN
    )


class Card(models.Model):
    class Suit(models.IntegerChoices):
        pass


class MyModel(models.Model):
    MY_CHOICES = (
        ('Option1' , 'Option1') ,
        ('Option2' , 'Option2') ,
        ('Option3' , 'Option3') ,
    )

    my_field = models.CharField(
        max_length=20 ,
        choices=MY_CHOICES
    )

    def __str__(self):
        return f"{self.pk} - {self.my_field}"

    class Meta:
        pass
