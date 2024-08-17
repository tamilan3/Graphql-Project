import random
from django.core.management.base import BaseCommand
from myappapp.models import Author, Book
from faker import Faker
from datetime import date

class Command(BaseCommand):
    help = 'Generate dummy data for Book models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate Authors
        authors = []
        for _ in range(10):  # Generate 10 authors
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth_date = fake.date_of_birth(minimum_age=30, maximum_age=70)
            email = fake.email()
            author = Author.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date, email=email)
            authors.append(author)

        # Generate Books
        for _ in range(100):  # Generate 30 books
            title = fake.sentence(nb_words=4)
            publication_date = fake.date_this_century()
            isbn = fake.isbn13()
            pages = random.randint(100, 1000)
            cover = fake.image_url()
            language = fake.language_name()
            book_image = None  # or set a default image path if required
            author = random.choice(authors)
            Book.objects.create(title=title, publication_date=publication_date, isbn=isbn, pages=pages,
                                cover=cover, language=language, book_image=book_image, author=author)

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data for Authors and Books.'))