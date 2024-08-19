from graphene import relay
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from myappapp.models import Author, Book


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ("username", "email")
        fields = ("id", "username", "email")
        interfaces = (relay.Node,)
        
        
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ("birth_date", "email")
        fields = ("id", "first_name", "last_name", "birth_date", "email") 
        interfaces = (relay.Node,)

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = ("title",)
        fields = ("id", "title", "publication_date", "isbn", "pages", "cover", "language", "book_image", "author") 
        interfaces = (relay.Node,)