import graphene  
from graphene_django.filter import DjangoFilterConnectionField
from myappapp.models import Author, Book
from ..types.types import AuthorType, BookType
from ..filters.author import AuthorFilter
from ..filters.book import BookFilter

class Query(graphene.ObjectType):
    all_authors = DjangoFilterConnectionField(AuthorType,filterset_class=AuthorFilter)
    all_books = DjangoFilterConnectionField(BookType,filterset_class=BookFilter)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    book_by_id = graphene.Field(BookType, id=graphene.Int(required=True))
    me = graphene.Field(AuthorType)  # Assuming you want to return the current user

    def resolve_all_authors(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return Author.objects.all()

    def resolve_all_books(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return Book.objects.all()

    def resolve_author_by_id(self, info, id):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return None

    def resolve_book_by_id(self, info, id):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return None

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication credentials were not provided')
        return user
