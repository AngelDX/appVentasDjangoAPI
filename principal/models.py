from django.db import models

TYPES = (
        ('VOLADOR', 'Volador'),
        ('VELOCIDAD', 'Velocidad'),
        ('ATAQUE', 'Ataque'),
    )

class Hero(models.Model):
	name=models.CharField(max_length=60)
	alias=models.CharField(max_length=60)

	def __str__(self):
		return self.name



class Powers(models.Model):
	hero=models.ManyToManyField(Hero)
	power=models.CharField(max_length=30)
	type=models.CharField(max_length=20,choices=TYPES)

	def __str__(self):
		return self.power
