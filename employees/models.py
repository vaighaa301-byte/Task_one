from django.db import models


class Employee(models.Model):
	class Status(models.TextChoices):
		ACTIVE = 'Active', 'Active'
		INACTIVE = 'Inactive', 'Inactive'

	employee_id = models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=120)
	email = models.EmailField()
	phone = models.CharField(max_length=30)
	department = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)
	date_of_joining = models.DateField()
	status = models.CharField(max_length=8, choices=Status.choices, default=Status.ACTIVE)

	class Meta:
		ordering = ['name', 'employee_id']

	def __str__(self):
		return f'{self.employee_id} - {self.name}'

# Create your models here.
