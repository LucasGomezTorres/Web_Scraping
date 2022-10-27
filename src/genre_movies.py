"""
Description: This file contains the logic necessary to extract 
            information from the movies that make up a movie genre. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

import requests
from bs4 import BeautifulSoup

def genre_movies_extraction(genre_name, genre_url):
    """
    Function that allows you to extract information from movie cards, such as: 
    identifier, title, duration, rating, description, actors, etc.

    Inputs:
        - genre_name: Name identifying the genre of the movies
        - genre_url: URL to access the page where to extract information
    """

    # Data structure to store all the information
    genre_movies = {}

    # Get all the text of the page identified by the input URL
    response = requests.get(genre_url)
    soup = BeautifulSoup(response.text, features="lxml")

    # Get all movies
    all_movies = soup.find_all("div", {"class": "lister-item-content"})

    # Get the information card for each movie
    for movie_info in all_movies:

        # Get movie title
        raw_movie_title = movie_info.find_all("h3")
        if raw_movie_title!= None:
            movie_title = raw_movie_title[0].get_text().replace("\n", "")
            movie_id = int(movie_title.split('.')[0])

        # Get movie duration
        raw_movie_duration = movie_info.find("span", {"class": "runtime"})
        if raw_movie_duration!= None:
            movie_duration = raw_movie_duration.get_text().replace("\n", "")

        # Get movie rating
        raw_movie_rating = movie_info.find("div", {"class": "inline-block ratings-imdb-rating"})
        if raw_movie_rating!= None:
            movie_rating = raw_movie_rating.get_text().replace("\n", "")

        # Get movie description
        raw_movie_description = movie_info.find_all("p", {"class": "text-muted"})
        if raw_movie_description!= None:
            movie_description = raw_movie_description[-1].get_text().replace("\n", "")

        # Get movie stars
        raw_movie_stars = movie_info.find("p", {"class": ""})
        if raw_movie_stars!= None:
            movie_stars = raw_movie_stars.get_text().replace("\n", "").split('Stars:')[1]

        # Get the movie votes
        raw_movie_votes = movie_info.find("span", {"name": "nv"})
        if raw_movie_votes!= None:
            movie_votes = raw_movie_votes.get_text().replace("\n", "")

        # Storage of information in the data structure
        genre_movies[f"{genre_name}_movie_{movie_id}"] = {
            'Movie Title': movie_title,
            'Movie Duration': movie_duration,
            'Movie Rating': movie_rating,
            'Movie Description': movie_description,
            'Movie Starts': movie_stars,
            'Movie Votes': movie_votes
            }

    return genre_movies