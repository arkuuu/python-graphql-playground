from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = gql("""
    type Query {
        hello: String!
        greeting(name: String!): String!
    }
""")

# Create type instance for Query type defined in our schema...
query = QueryType()

# ...and assign our resolver function to its "hello" field.
@query.field("hello")
def resolve_hello(_, info) -> str:
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return f"Hello, {user_agent}!"

@query.field("greeting")
def resolve_greeting(*_, name: str) -> str:
    return f"Greetings, {name}!"

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)
