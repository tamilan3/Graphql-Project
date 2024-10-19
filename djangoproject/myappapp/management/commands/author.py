import random
from django.core.management.base import BaseCommand
from myappapp.models import Author, Book
from faker import Faker
from datetime import date

class Command(BaseCommand):
    help = 'Generate dummy data for Author and Book models'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(100):  # Generate 10 authors
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth(minimum_age=30, maximum_age=70)
            email = fake.email()
            author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date, email=email)
            author.save()

        
        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data for Authors and Books.'))
