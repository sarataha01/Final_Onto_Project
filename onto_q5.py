from rdflib import Graph, RDF, Namespace
from owlrl import DeductiveClosure, OWLRL_Semantics

# Define namespaces
BASE = Namespace(
    "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

# Load the ontology
graph = Graph()
graph.parse("final_phase1_onto_team6.ttl", format='ttl')
graph.parse("rules.ttl", format='ttl')

# Apply Deductive Closure reasoning with OWLRL Semantics to the graph
DeductiveClosure(OWLRL_Semantics).expand(graph)

# Get all the actor-directors from the ontology
actor_director = set()
for subj, pred, obj in graph:
    # Check if the subject is an ActorWriter
    if (subj, RDF.type, BASE.ActorDirector) in graph:
        actor_director.add(subj)

# Display the actor-directors
print("Persons that are ActorDirector:")
for director_writer_actor in actor_director:
    print(director_writer_actor)
