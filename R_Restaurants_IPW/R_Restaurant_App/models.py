from django.db import models

# Create your models here.

from django.db import models
import datetime


# Create your models here.

class Restaurant(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_name = models.CharField("Nom du restaurant", max_length=30)
    tva_nr = models.CharField('Numéro de TVA', max_length=15)
    y_launch = models.IntegerField("Année de lancement", default="1998")
    email_address = models.CharField("Adresse mail", max_length=30, default="monadresse@mail.com")
    city = models.CharField("Ville", max_length=30, default="Ville")

    has_employee = models.ManyToManyField("Employee")

    def __str__(self):
        return str(self.r_name)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField("Nom et prénom de l'employé", max_length=30, default='Nom')
    y_worked = models.IntegerField("Années d'ancienneté")
    job_choices = [("salle", "Salle"), ("cuisine", "Cuisine"), ("gestion", "Gestion")]
    job = models.CharField("Fonction", choices=job_choices, max_length=30, default="Salle, Cuisine ou Gestion")
    work_r = models.ManyToManyField(Restaurant, blank=True)

    def __str__(self):
        return str(self.e_name)

    class Meta:
        verbose_name = 'Employé'
        verbose_name_plural = 'Employés'


class Users(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username


class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    rating_choice = [('0', '0'), ('1', '1'), ('2', '2'), ('3','3'), ('4','4'), ('5','5')]
    rating = models.CharField(max_length=1, choices=rating_choice, default='0')
    time = models.DateTimeField("date et heure", auto_now_add=True)
    comment = models.CharField(max_length=300, blank=True)
    r_rated = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.r_rated) + " (" + str(self.id) + ')'

    class Meta:
        verbose_name = 'Avis'
        verbose_name_plural = 'Avis'
