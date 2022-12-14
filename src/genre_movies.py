"""
Description: This file contains the logic necessary to extract 
            information from the movies that make up a movie genre. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

from bs4 import BeautifulSoup
from get_images import get_image_movie
from get_videos import get_video_movie

def genre_movies_extraction(session,genre_name, genre_url, headers):
    """
    Function that allows you to extract information from movie cards, such as: 
    identifier, title, duration, rating, description, actors, etc.

    Inputs:
        - session: the session with cookies.
        - genre_name: Name identifying the genre of the movies
        - genre_url: URL to access the page where to extract information
    """

    # Data structure to store all the information
    genre_movies = {}

    # Get all the text of the page identified by the input URL
    response = session.get(genre_url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    # Get all movies
    all_movies = soup.find_all("div", {"class": "lister-item-content"})

    # Get the information card for each movie
    for movie_info in all_movies:
        # Get movie title
        raw_movie_title = movie_info.find_all("h3")
        if raw_movie_title!= None:
            movie_id_title_year = raw_movie_title[0].get_text().replace("\n", "").split('.')
            movie_id = movie_id_title_year[0]
            movie_title_raw = movie_id_title_year[1].split('(')
            movie_title = str(movie_title_raw[0])
            # Get movie year
            try:
                movie_year = movie_info.find("span", 
                        {"class": "lister-item-year text-muted unbold"}).get_text().split('(')[-1][:4]
            except: 
                movie_year = "NA"
        else: movie_title = "NA"  
        
        # Get movie duration
        raw_movie_duration = movie_info.find("span", {"class": "runtime"})
        if raw_movie_duration!= None:
            movie_duration = raw_movie_duration.get_text().replace("\n", "")
        else: movie_duration = "NA"

        # Get genres movie
        raw_movie_genres = movie_info.find("span", {"class": "genre"})
        if raw_movie_genres!= None:
            movie_genres = raw_movie_genres.get_text().replace("\n", "").strip()
        else: movie_genres = "NA"

        # Get movie rating
        raw_movie_rating = movie_info.find("div", {"class": "inline-block ratings-imdb-rating"})
        if raw_movie_rating!= None:
            movie_rating = raw_movie_rating.get_text().replace("\n", "")
        else: movie_rating = "NA"

        # Get my own movie rating
        raw_our_own_movie_rating = movie_info.find("span", {"class": "rating-rating rating-your"})
        if raw_our_own_movie_rating!= None:
            our_own_movie_rating = raw_our_own_movie_rating.get_text().replace("\n", "")
        else: our_own_movie_rating = "NA"

        # Get movie description
        raw_movie_description = movie_info.find_all("p", {"class": "text-muted"})
        if raw_movie_description!= None:
            movie_description = raw_movie_description[-1].get_text().replace("\n", "")
            if movie_description[:6] == 'Votes:' or movie_description.strip()[:9] == 'Director:':
                raw_movie_description = movie_info.find_all("p", {"class": ""})
                movie_description = raw_movie_description[-1].get_text().replace("\n", "")
        else: movie_description = "NA"

        # Get movie stars
        try: raw_movie_stars = movie_info.find_all("p", {"class": "text-muted text-small"})[1]
        except: raw_movie_stars = movie_info.find("p", {"class": ""})
        if raw_movie_stars!= None:
            try: movie_stars = raw_movie_stars.get_text().replace("\n", "").split('Stars:')[1]
            except: movie_stars = "NA"
        else: movie_stars = "NA"

        # Get the movie votes
        raw_movie_votes = movie_info.find("span", {"name": "nv"})
        if raw_movie_votes!= None:
            movie_votes = raw_movie_votes.get_text().replace("\n", "")
        else: movie_votes = "NA"

        # Get movie image
        movie_image = get_image_movie(soup,movie_info,movie_id,genre_name,headers,only_url=True)

        # Get movie video
        movie_video = get_video_movie(soup,movie_info,movie_id,genre_name,headers,only_url=True)

        # Storage of information in the data structure
        genre_movies[f"{genre_name}_movie_{movie_id}"] = {
            'Movie Title': movie_title,
            'Movie Year': movie_year,
            'Movie Duration': movie_duration,
            'Movie Genres': movie_genres,
            'Movie Rating': movie_rating,
            'Our Rating': our_own_movie_rating,
            'Movie Description': movie_description,
            'Movie Stars': movie_stars,
            'Movie Votes': movie_votes,
            'Movie Image': movie_image,
            'Movie Video': movie_video
            }

    return genre_movies