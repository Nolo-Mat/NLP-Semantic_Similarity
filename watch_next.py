import spacy

def find_similar_movie(description):
    movies = []
    with open('movies.txt', 'r') as file:
        movies = file.readlines()
    
    # Cleaning up the movie descriptions
    movies = [movie.strip().split(':', 1)[1].strip() for movie in movies]
    
    # Loading the spaCy language model
    nlp = spacy.load('en_core_web_md')
    
    # Calculating the similarity between the input description and each movie description
    similarity_scores = [nlp(description).similarity(nlp(movie)) for movie in movies]
    
    # Finding the index of the most similar movie
    most_similar_index = similarity_scores.index(max(similarity_scores))
    
    # Retrieving the title of the most similar movie
    most_similar_movie = movies[most_similar_index]
    return most_similar_movie

# Test the function
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
next_movie = find_similar_movie(input_description)
print("Next movie to watch:", next_movie)

