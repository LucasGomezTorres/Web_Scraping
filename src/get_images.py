"""
Description: This file contains the logic necessary to extract 
            information from the names and urls of the movie genres. 

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
#!pip install webdriver-manager
import chromedriver_binary 
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from tqdm import tqdm
from urllib.parse import urlparse

if __name__ == "__main__":
    print("hola")
    print(os.getcwd())
    url_comedia = 'https://www.imdb.com/search/title?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=NK3CZ9827P3B9WEDPFZN&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1'
   
    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
            */*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "en-US,en;q=0.8",
            "Cache-Control": "no-cache",
            "dnt": "1",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36\
                (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

    # Get all the text of the page identified by the input URL
    response = requests.get(url_comedia, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    print("hola")
    # URL imdb
    imdb_url = 'https://www.imdb.com'

    # Get all urls movies for image and video
    all_movies = soup.find_all("div", {"class": "lister-item-content"})

    # Get the urls of the photos and videos of the films
    urls_photos_videos = [movie_info.find('a').get("href") for movie_info in all_movies]

    # Get the abs urls
    abs_urls_photos_videos = [urllib.parse.urljoin(imdb_url,url) for url in urls_photos_videos]

    abs_url_prueba = abs_urls_photos_videos[4]
    abs_url_prueba
    # Get all the text of the page identified by the input URL
    response = requests.get(abs_url_prueba, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    # Get all urls movies for image and video
    photo_img = soup.find("div", {"class": "ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img"})
    for i in photo_img:
        foto = i.get("srcset").split(',')[0]

    img_data = requests.get(foto).content
    with open('src/images_films/comedia_111112.jpg', 'wb') as handler:
        handler.write(img_data)

