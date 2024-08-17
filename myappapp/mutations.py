import graphene
import graphql_jwt
from myappapp.models import Author, Book
from .types import AuthorType, BookType, UserType



class CreateAuthor(graphene.Mutation):
    author = graphene.Field(AuthorType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth_date = graphene.Date(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, first_name, last_name, birth_date, email):
        author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date, email=email)
        author.save()
        return CreateAuthor(author=author)

class UpdateAuthor(graphene.Mutation):
    author = graphene.Field(AuthorType)

    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        birth_date = graphene.Date()
        email = graphene.String()

    def mutate(self, info, id, first_name=None, last_name=None, birth_date=None, email=None):
        author = Author.objects.get(pk=id)
        if first_name:
            author.first_name = first_name
        if last_name:
            author.last_name = last_name
        if birth_date:
            author.birth_date = birth_date
        if email:
            author.email = email
        author.save()
        return UpdateAuthor(author=author)

class DeleteAuthor(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        author = Author.objects.get(pk=id)
        author.delete()
        return DeleteAuthor(success=True)

class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        title = graphene.String(required=True)
        publication_date = graphene.Date(required=True)
        isbn = graphene.String(required=True)
        pages = graphene.Int(required=True)
        cover = graphene.String(required=True)
        language = graphene.String(required=True)
        author_id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, title, publication_date, isbn, pages, cover, language, author_id, book_image):
        author = Author.objects.get(pk=author_id)
        book = Book(
            title=title,
            publication_date=publication_date,
            isbn=isbn,
            pages=pages,
            cover=cover,
            language=language,
            author=author,
            book_image=book_image
        )
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        publication_date = graphene.Date()
        isbn = graphene.String()
        pages = graphene.Int()
        cover = graphene.String()
        language = graphene.String()

    def mutate(self, info, id, title=None, publication_date=None, isbn=None, pages=None, cover=None, language=None):
        book = Book.objects.get(pk=id)
        if title:
            book.title = title
        if publication_date:
            book.publication_date = publication_date
        if isbn:
            book.isbn = isbn
        if pages:
            book.pages = pages
        if cover:
            book.cover = cover
        if language:
            book.language = language
        book.save()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBook(success=True)


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)
    
class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()