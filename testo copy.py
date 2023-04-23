import imdb

# Create an instance of IMDb
ia = imdb.IMDb()

# Ask the user for their preferred movie genre
genre = input("What genre of movies do you like? ")

# Search for the top 10 movies in the user's preferred genre
search_results = ia.search_movie(genre)
top_movies = []
for result in search_results:
    movie = ia.get_movie(result.getID())
    if genre.lower() in [g.lower() for g in movie['genres']]:
        top_movies.append(movie)
    if len(top_movies) == 10:
        break

# Print the top 10 movies
print("Here are the top 10 movies in the", genre, "genre:")
for i, movie in enumerate(top_movies):
    print(i+1, "-", movie['title'], "(" + str(movie['year']) + ")")

# Ask the user for a movie title they enjoyed
liked_movie_title = input("What's a movie you enjoyed? ")

# Search for the movie the user liked
liked_movie = ia.search_movie(liked_movie_title)[0]
liked_movie = ia.get_movie(liked_movie.getID())

# Get recommendations based on the user's liked movie
recommendations = ia.get_recommendations(liked_movie)
print("Here are some movies you might also enjoy:")
for i, movie in enumerate(recommendations[:10]):
    print(i+1, "-", movie['title'], "(" + str(movie['year']) + ")")
