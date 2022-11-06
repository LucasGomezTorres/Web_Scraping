"""
Description: This file contains the logic necessary to download 
            the videos of the movies. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

# Se importan las librerías que se van a usar
import requests
import pandas as pd
import urllib.parse
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse


def get_video_movie(soup,movie_info,movie_id,genre_name,headers,only_url=True):

    """
    Function that allows you to download the video from movie and it returns the video download url

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
    url_video = movie_info.find('a').get("href")

    # Get the absolutes paths of the photos and videos of the films
    abs_url_video = urllib.parse.urljoin(imdb_url,url_video)

    # Get all the text of the page identified by the input URL
    response = requests.get(abs_url_video, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    # Get url movie for download the video 
    soup_video = soup.find_all("a",class_="ipc-lockup-overlay ipc-focusable")
    url_video = [i.get("href") for i in soup_video].pop(1)

    # Get the absolute url for download the video
    abs_url_video = urllib.parse.urljoin(imdb_url,url_video) 
    #print(abs_url_video + "id" + str(movie_id))

    # Get all the text of the page identified by the input URL
    response = requests.get(abs_url_video, headers=headers)
    soup_video_url = BeautifulSoup(response.text, features="html.parser") 
    
    # Get string json
    try:
        json_string = soup_video_url.find('script', id='__NEXT_DATA__', type='application/json').string
    except AttributeError as e:
        json_string = None

    # Load the json with information about the url of video
    try:
        json_data = json.loads(json_string)
    except TypeError as e:
        json_data =  None
    except AttributeError as e:
        json_data =  None

    # Get url movie for download the image 
    try:
        url_video_download = json_data['props']['pageProps']['videoPlaybackData']['video']['playbackURLs'][1]['url']
    except KeyError as e:
        url_video_download = 'NA'
    except TypeError as e:
        url_video_download = 'NA'

    # Return only the access URL
    if only_url:
        return url_video_download
        
    else:
        # Get the video of film and save to videos_film folder 
        video_data = requests.get(url_video_download,stream=True,headers=headers).content
        with open('src/videos_films/'+genre_name+'_'+str(movie_id)+'.mp4', 'wb') as handler:
            handler.write(video_data)
            print("download video"+str(movie_id))
            return '/videos_films/'+genre_name+'_'+str(movie_id)+'.mp4'


