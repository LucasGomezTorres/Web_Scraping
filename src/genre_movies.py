"""
Description:


Authors: 
    Lucas Gómez, Joan Amengual
"""

import requests
import os
import urllib.parse
from bs4 import BeautifulSoup

def extract_info(genre_url):

    # Get all the text of the page identified by the input URL
    response = requests.get(genre_url)
    soup = BeautifulSoup(response.text, features="lxml")

    # Get all movies
    all_movies = soup.find_all("div", {"class": "lister-item-content"})

    # Get the information card for each movie
    for movie_info in all_movies:

        # Get movie title
        movie_title = movie_info.find_all("h3")
        print(movie_title[0].get_text())

        # Get movie duration
        movie_duration = movie_info.find("span", {"class": "runtime"})
        print(movie_duration.get_text())

        # Get movie rating
        movie_rating = movie_info.find("div", {"class": "inline-block ratings-imdb-rating"})
        print(movie_rating.get_text())

        # Get movie description
        movie_description = movie_info.find_all("p", {"class": "text-muted"})
        print(movie_description[-1].get_text())

        # Get movie stars
        movie_stars = movie_info.find("p", {"class": ""})
        print(movie_stars.get_text())

        # Get the movie votes
        movie_votes = movie_info.find("span", {"name": "nv"})
        print(movie_votes.get_text())

        # TODO: Remove this brake to enable routing for all movies when the operations are ready 
        break

if __name__ == "__main__":
    # Starting URL to get the information of the movies
    genre_url = "https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=MCMWMC4F4V3YRQFB7292&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1"

    extract_info(genre_url)