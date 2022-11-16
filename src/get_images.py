"""
Description: This file contains the logic necessary to download 
            the imageo of the movies. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

# Se importan las librerías que se van a usar
import requests
import time
import re
import pandas as pd
import os
import urllib.parse
import chromedriver_binary 
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urlparse


def get_image_movie(soup,movie_info,movie_id,genre_name,headers,only_url=True):

    """
    Function that allows you to download the image from movie and it returns the image download url

    Inputs:
        - soup: the text of the page identified by the input URL
        - movie_info: text of the movie in html format
        - movie_id: unique id of each movie
        - genre_name: name identifying the genre of the movie
        - headers: information for modifying the user-agent
    """

    # URL imdb to get the absolute path of the images
    imdb_url = 'https://www.imdb.com'

    # Get the relative paths of the photos and videos of the films
    url_photo = movie_info.find('a').get("href")

    # Get the absolutes paths of the photos and videos of the films
    abs_url_photo = urllib.parse.urljoin(imdb_url,url_photo)

    # Get all the text of the page identified by the input URL
    response = requests.get(abs_url_photo, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    # Get url movie for download the image 
    image_poster = soup.find("div", {"class": "ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img"})
    for image_poster_content in image_poster:
        url_image = image_poster_content.get("srcset").split(',')[0]

    # Return only the access URL
    if only_url:
        return url_image
    else:
        # Get the image of film and save to images_film folder 
        image_data = requests.get(url_image,headers=headers).content
        with open('src/images_films/'+genre_name+'_'+str(movie_id)+'.jpg', 'wb') as handler:
            handler.write(image_data)
            print("download image"+str(movie_id))
            return '/images_films/'+genre_name+'_'+str(movie_id)+'.jpg'


