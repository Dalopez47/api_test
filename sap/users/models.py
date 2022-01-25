from django.db import models

class User (models.Model):

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    proImage = models.ImageField(null=True, blank=True)
    email = models.CharField(max_length=100, unique=True)
    birthdate = models.DateTimeField()
    wPhone = models.CharField(max_length=100)
    pPhone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    def __str__(self):
        return f'Persona {self.id}: {self.name} {self.lastname} {self.company} {self.email } {self.birthdate}' \
               f'{self.wPhone}{self.pPhone}{self.address} {self.city}'



