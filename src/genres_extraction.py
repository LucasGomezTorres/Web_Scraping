"""
Description: This file contains the logic necessary to extract 
            information from the names and urls of the movie genres. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

import requests
from bs4 import BeautifulSoup

def genres_names_urls_extraction(session,genres_url,headers):

    """
    Function that allows you to extract the names and urls from the movie genres.

    Inputs:
        - session: the session with cookies. 
        - genres_url: URL initial to access the page where to extract information.
        - headers: information for modifying the user-agent.

    """

    # Get all the text of the page identified by the input URL
    response = session.get(genres_url,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")

    # Get all the text of the page identified by the input URL
    genres = soup.find_all(attrs={'class': 'image'}) 

    # Get the urls of the genres of the films
    urls_genres = [x.get('href') for genre in genres  for x in genre.findChildren('a')]

    # Get the names of the genres of the films
    names_genres = [x.get('alt') for genre in genres  for x in genre.findChildren('img')]

    # Create the dict_genres
    dict_genres = {names_genres[i]: urls_genres[i] for i in range(len(names_genres))}

    return dict_genres
