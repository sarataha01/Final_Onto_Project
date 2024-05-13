from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF

g = Graph()
g.parse("final_phase1_onto_team6.ttl", format="turtle")

# Define namespaces used in the ontology
ontology_ns = Namespace(
    "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/")

# Read the SPARQL query pattern from the text file
with open("q2_query.txt", "r") as file:
    query_pattern = file.read()

# Prepare the SPARQL query
query = prepareQuery(query_pattern, initNs={
                     "rdf": RDF, "ontology_ns": ontology_ns})

# Execute the query and process the results
for row in g.query(query):
    individual = row.individual
    gender = row.gender
    age = row.age
    name = row.name
    nationality = row.nationality

    # Print details of the individual
    print("Individual:", individual)
    print("Gender:", gender)
    print("Age:", age)
    print("Name:", name)
    print("Nationality:", nationality)
    print()
