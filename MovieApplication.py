from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, XSD

# Define a Movie class to represent each movie


class Movie:
    def __init__(self, title, actors, director, genres, year):
        self.title = title
        self.actors = actors
        self.director = director
        self.genres = genres
        self.year = year

# Define a class to manage the movie database


class MovieDatabase:
    def __init__(self):
        self.movies = []

    def load_from_ttl(self, ttl_file):
        g = Graph()
        g.parse(ttl_file, format="ttl")

        for movie_uri in g.subjects(RDF.type, URIRef("http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/Movies")):
            title = str(g.value(movie_uri, URIRef(
                "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/hasTitle")))
            actors = [str(actor) for actor in g.objects(movie_uri, URIRef(
                "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/hasActor"))]
            director = str(g.value(movie_uri, URIRef(
                "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/hasDirector")))
            genres = [str(genre) for genre in g.objects(movie_uri, URIRef(
                "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/hasGenre"))]
            year = int(g.value(movie_uri, URIRef(
                "http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/hasYear")))

            movie = Movie(title, actors, director, genres, year)
            self.movies.append(movie)

    def search_movies(self, included_actors=[], included_directors=[], included_genres=[], excluded_actors=[], excluded_directors=[], excluded_genres=[]):
        result = []

        for movie in self.movies:
            # Check if the movie satisfies the inclusion criteria
            include_condition = (not included_actors or set(movie.actors).intersection(included_actors)) \
                and (not included_directors or movie.director in included_directors) \
                and (not included_genres or set(movie.genres).intersection(included_genres))

            # Check if the movie satisfies the exclusion criteria
            exclude_condition = (not excluded_actors or not set(movie.actors).intersection(excluded_actors)) \
                and (not excluded_directors or movie.director not in excluded_directors) \
                and (not excluded_genres or not set(movie.genres).intersection(excluded_genres))

            # If the movie satisfies both inclusion and exclusion criteria, add it to the result
            if include_condition and exclude_condition:
                result.append(movie)

        return result


# Main function
def main():
    # Create a movie database
    movie_database = MovieDatabase()

    ontology_link = 'http://www.semanticweb.org/future/ontologies/2024/4/untitled-ontology-2/'

    # Load movie data from TTL file
    movie_database.load_from_ttl("final_phase1_onto_team6.ttl")

    # Prompt the user for actor names
    included_actor_names = input(
        "Enter actor names you want to include separated by commas: ").split(',')
    # Check if included_actor_names is empty
    included_actor_uris = [ontology_link + actor.strip()
                           for actor in included_actor_names]

    # Prompt the user for actor names
    excluded_actor_names = input(
        "Enter actor names you want to exclude separated by commas: ").split(',')
    # Check if excluded_actor_names is empty
    excluded_actor_uris = [ontology_link + actor.strip()
                           for actor in excluded_actor_names]

    # Prompt the user for genre types
    included_genre_types = input(
        "Enter genre types you want to include separated by commas: ").split(',')
    # Check if included_genre_types is empty
    included_genre_uris = [ontology_link + genre.strip()
                           for genre in included_genre_types]

    # Prompt the user for genre types
    excluded_genre_types = input(
        "Enter genre types you want to exclude separated by commas: ").split(',')
    # Check if excluded_genre_types is empty
    excluded_genre_uris = [ontology_link + genre.strip()
                           for genre in excluded_genre_types]

    # Prompt the user for director names
    included_director_names = input(
        "Enter director names you want to include separated by commas: ").split(',')
    # Check if included_director_names is empty
    included_director_uris = [ontology_link + director.strip()
                              for director in included_director_names]

    # Prompt the user for director names
    excluded_director_names = input(
        "Enter director names you want to exclude separated by commas: ").split(',')
    # Check if excluded_director_names is empty
    excluded_director_uris = [ontology_link + director.strip()
                              for director in excluded_director_names]

    # Check if any of the lists are empty and replace them with []
    included_actor_uris = included_actor_uris if included_actor_uris != [
        ontology_link] else []
    excluded_actor_uris = excluded_actor_uris if excluded_actor_uris != [
        ontology_link] else []
    included_director_uris = included_director_uris if included_director_uris != [
        ontology_link] else []
    excluded_director_uris = excluded_director_uris if excluded_director_uris != [
        ontology_link] else []
    included_genre_uris = included_genre_uris if included_genre_uris != [
        ontology_link] else []
    excluded_genre_uris = excluded_genre_uris if excluded_genre_uris != [
        ontology_link] else []

    # Search for movies based on criteria
    found_movies = movie_database.search_movies(
        included_actors=included_actor_uris,
        included_genres=included_genre_uris,
        included_directors=included_director_uris,
        excluded_actors=excluded_actor_uris,
        excluded_genres=excluded_genre_uris,
        excluded_directors=excluded_director_uris,
    )

    # Display the found movies
    if found_movies:
        print("Found movies:")
        for movie in found_movies:
            print("Title:", movie.title)
            print("Year:", movie.year)
            print("Genres:", ", ".join(movie.genres))
            print("Director:", movie.director)
            print("Actors:", ", ".join(movie.actors))
            print("----------")
    else:
        print("No movies found matching the criteria.")


if __name__ == "__main__":
    main()
