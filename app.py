from ariadne import QueryType, ObjectType, gql, make_executable_schema
from ariadne.asgi import GraphQL

from data import origins as DATA


# SDL
type_defs = gql("""
    type Origin {
        url: String!
        visits: [OriginVisit]!
        snapshots: [Snapshot]!
        revisions: [Revision]!
    }

    type OriginVisit {
        origin: Origin!
        snapshot: Snapshot!
        status: String!
    }

    type Snapshot {
        date: String!   # Can be a defined scalar as well
        revisions: [Revision!]!
        origin: Origin!
        visit: OriginVisit!
    }

    type Revision {
        message: String
        snapshots: [Snapshot]!
        origin: Origin!
    }

    type Query {
        origins(first: Int = 10): [Origin]
        origin(like: String!): Origin
        visit(id: String!): OriginVisit
    }
""")

query = QueryType()
origin = ObjectType('Origin')
visit = ObjectType('OriginVisit')

@query.field('origins')
def resolve_origins(_, info, **args):
    limit = args.get('first', 10)
    # query origin obj
    return DATA


@query.field('origin')
def resolve_origin(*_, **args):
    for each in DATA:
        if args['like'] in each['url']:
            return each
    return None

@origin.field('visits')
def resolve_visit_origin(obj, *_):
    # query with visit object
    return obj['visits']

@visit.field('origin')
def resolve_visit_origin(obj, *_):
    # query with visit object
    return {
        'url': 'http://test',
        'visits': []
    }

# Eg just has query (avoiding Mutations and subscriptions)
schema = make_executable_schema(type_defs, query, origin, visit)
# Run using any ASGI server (Uvicorn)
app = GraphQL(schema, debug=True)
