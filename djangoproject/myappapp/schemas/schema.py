import graphene
from ..queries.queries import Query
from ..mutations.mutations import Mutation

schema = graphene.Schema(query=Query,mutation=Mutation)


