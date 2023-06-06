# Movie Recommendation Bot

import random
import imdb

def get_movie_recommendation(genre):
    ia = imdb.IMDb()

    # Search for movies based on the genre
    movies = ia.search_movie(genre)

    if not movies:
        return "Sorry, I couldn't find any movies in that genre."

    # Select a random movie from the search results
    movie = random.choice(movies)

    # Retrieve the movie details
    ia.update(movie)
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    plot = movie["plot"][0]

    recommendation = f"Title: {title}\nYear: {year}\nRating: {rating}\nPlot: {plot}"

    return recommendation

def main():
    print("Welcome to the Movie Recommendation Bot!")
    print("Enter a genre and I'll recommend a movie for you.")

    while True:
        genre = input("Enter a movie genre (e.g., action, comedy, romance): ")

        if genre.lower() == "exit":
            break

        recommendation = get_movie_recommendation(genre)

        print("\nRecommendation:")
        print(recommendation)
        print()

if __name__ == "__main__":
    main()
