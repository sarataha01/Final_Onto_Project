from rdflib import Graph, Namespace
from rdflib.tools.rdf2dot import rdf2dot
from io import StringIO
import subprocess

g = Graph()
g.parse("final_phase1_onto_team6.ttl", format="turtle")

# Define namespaces used in the ontology
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
ontology_ns = Namespace(
    "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/")

# Define the Persons class
Actor = ontology_ns.Actor
Writer = ontology_ns.Writer
Director = ontology_ns.Director

# Define a set to store processed individuals
processed_individuals = set()

# Iterate through all subjects in the graph
for subject in g.subjects():
    # Check if the subject is of type Actor, Writer, or Director
    if (subject, rdf.type, Actor) in g or (subject, rdf.type, Writer) in g or (subject, rdf.type, Director) in g:
        # Check if the individual has already been processed
        if subject not in processed_individuals:
            # Print details of the individual
            print("Individual:", subject)
            print("Gender:", g.value(subject, ontology_ns.hasGender))
            print("Age:", g.value(subject, ontology_ns.hasAge))
            print("Name:", g.value(subject, ontology_ns.hasName))
            print("Nationality:", g.value(subject, ontology_ns.hasNationality))
            print()

            # Add the individual to the set of processed individuals
            processed_individuals.add(subject)

# Convert RDF graph to dot format
stream = StringIO()
rdf2dot(g, stream)
dot_representation = stream.getvalue()

# Save dot representation to a file
dot_path = "rdf_graph.dot"
with open(dot_path, "w") as f:
    f.write(dot_representation)

# Use Graphviz to render an image
output_image_path = "rdf_graph.png"
subprocess.run(["dot", "-Tpng", dot_path, "-o", output_image_path])

print(f"RDF graph image saved at: {output_image_path}")
