from rdflib import Graph, RDF, Namespace, Literal
from owlrl import DeductiveClosure, RDFS_Semantics

# Load TTL file
g = Graph()
g.parse("final_phase1_onto_team6.ttl", format='ttl')
DeductiveClosure(RDFS_Semantics).expand(g)

# Define namespace
ns = Namespace(
    "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/")

# Get movie name from user
movie_name = input("Enter the name of the movie: ")

# Find movie information
movie_found = False
for subj, _, _ in g.triples((None, RDF.type, ns.Movies)):
    if (subj, ns.hasTitle, Literal(movie_name)) in g:
        movie_info = {
            'Year': g.value(subj, ns.hasYear),
            'Country': g.value(subj, ns.hasCountry),
            'Genres': list(g.objects(subj, ns.hasGenre)),
            'Actors': list(g.objects(subj, ns.hasActor))
        }
        movie_found = True
        break

# Display movie information or error message
if movie_found:
    print("Movie Information:")
    print("Name:", movie_name)
    print("Year:", movie_info.get('Year'))
    print("Country:", movie_info.get('Country'))
    print("Genres:", ', '.join(movie_info.get('Genres')))
    print("Actors:", ', '.join(movie_info.get('Actors')))
else:
    print("Error: Movie '{}' not found.".format(movie_name))
