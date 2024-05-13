from rdflib import Graph, Namespace, RDF
from owlrl import DeductiveClosure, OWLRL_Semantics

# Define namespaces
BASE = Namespace(
    "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

# Load the TTL file into an RDF graph
g = Graph()
g.parse("final_phase1_onto_team6.ttl", format='ttl')
g.parse("rules.ttl", format='ttl')

# Apply Deductive Closure reasoning with OWLRL Semantics to the graph
DeductiveClosure(OWLRL_Semantics).expand(g)

# Get all ActorWriters from the ontology
actor_writers = set()
for subj, pred, obj in g:
    if (subj, RDF.type, BASE.ActorWriter) in g:
        actor_writers.add(subj)

# Display ActorWriters
print("Persons that are ActorWriter:")
for actor_writer in actor_writers:
    print(actor_writer)

# Get all WriterDirectors from the ontology
director_writers = set()
for subj, pred, obj in g:
    if (subj, RDF.type, BASE.WriterDirector) in g:
        director_writers.add(subj)

# Display WriterDirectors
print("Persons that are DirectorWriter:")
for director_writer in director_writers:
    print(director_writer)

# Get all ActorWriterDirectors from the ontology
director_writers_actor = set()
for subj, pred, obj in g:
    if (subj, RDF.type, BASE.ActorWriterDirector) in g:
        director_writers_actor.add(subj)

# Display ActorWriterDirectors
print("Persons that are DirectorWriterActor:")
for director_writer_actor in director_writers_actor:
    print(director_writer_actor)
