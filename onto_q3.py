from rdflib import Graph, Namespace
from rdflib.namespace import RDF
from owlrl import DeductiveClosure, RDFS_Semantics

# Load the ontology graph
g = Graph()
g.parse("final_phase1_onto_team6.ttl", format="turtle")

# Define namespaces used in the ontology
ontology_ns = Namespace(
    "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/")

# Define the Persons class
Actor = ontology_ns.Actor

# Apply RDFS semantics for deductive closure
DeductiveClosure(RDFS_Semantics).expand(g)

# Iterate over individuals inferred to be of type Actor
print("Actors:")
for actor in g.subjects(RDF.type, Actor):
    print(actor)
