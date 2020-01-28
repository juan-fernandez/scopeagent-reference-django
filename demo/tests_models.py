import logging
import os
import requests

from django.test import TestCase
from demo.models import Person


class UnitTests(TestCase):
    def test_can_create_and_search_for_and_delete_person(self):
        new_person = Person.objects.create(first_name='John', last_name='Doe')
        self.assertEqual(new_person.first_name, 'John')
        self.assertEqual(new_person.last_name, 'Doe')
        person = Person.objects.filter(first_name='John').first()
        self.assertEqual(person.first_name, 'John')
        self.assertEqual(person.last_name, 'Doe')
        person.delete()
        count = Person.objects.filter(first_name='John').count()
        self.assertEqual(count, 0)
    
    def test_can_fetch_data(self):
        response = requests.get('https://www.google.com')
        self.assertEqual(response.status_code, 200)
        
