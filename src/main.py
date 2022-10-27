"""
Description:


Authors: 
    Lucas Gómez, Joan Amengual
"""

from genre_movies import genre_movies_extraction
from genres_extraction import genres_names_urls_extraction

def main():

    # Modifying the user-agent
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

    print("1. URL and names genres extraction:")
    genres_url = "https://www.imdb.com/feature/genre"

    print("Genres:" + str(genres_names_urls_extraction(genres_url,headers)))
    genres = genres_names_urls_extraction(genres_url,headers)
    print("\n")

    print("2. Extraction of information from movies of each genre")
    print("\n")
    for genre_name in list(genres.keys()):
        print("\n >>>>>>> Genre: " +genre_name+ " <<<<<<< \n" )
        genre_url = genres[genre_name] 
        print(f"{genre_name} movies:" + str(genre_movies_extraction(genre_name, genre_url, headers)))

    print("3. Extraction of information from a movie")

if __name__ == "__main__":
    main()