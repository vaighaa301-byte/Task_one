from datetime import date

from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeViewsTests(TestCase):
	def setUp(self):
		self.employee = Employee.objects.create(
			employee_id='EMP-001',
			name='Avery Morgan',
			email='avery@example.com',
			phone='+1-555-0101',
			department='Engineering',
			designation='Developer',
			date_of_joining=date(2024, 3, 11),
		)

	def test_employee_list_shows_employees(self):
		response = self.client.get(reverse('employees:list'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Avery Morgan')
		self.assertContains(response, 'EMP-001')

	def test_employee_detail_shows_all_fields(self):
		response = self.client.get(reverse('employees:detail', args=[self.employee.pk]))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'avery@example.com')
		self.assertContains(response, 'Engineering')
		self.assertContains(response, 'March 11, 2024')

	def test_missing_employee_returns_404(self):
		response = self.client.get(reverse('employees:detail', args=[9999]))

		self.assertEqual(response.status_code, 404)


class EmployeeModelTests(TestCase):
	def setUp(self):
		self.employee = Employee.objects.create(
			employee_id='EMP-001',
			name='Avery Morgan',
			email='avery@example.com',
			phone='+1-555-0101',
			department='Engineering',
			designation='Developer',
			date_of_joining=date(2024, 3, 11),
		)

	def test_employee_id_must_be_unique(self):
		with self.assertRaises(IntegrityError), transaction.atomic():
			Employee.objects.create(
				employee_id='EMP-001',
				name='Another Person',
				email='another@example.com',
				phone='555-0102',
				department='People',
				designation='Coordinator',
				date_of_joining=date(2025, 1, 6),
			)

# Create your tests here.
