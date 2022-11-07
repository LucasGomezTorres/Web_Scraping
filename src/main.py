"""
Description: Main file

Authors: 
    Lucas Gómez, Joan Amengual
"""
import os
import pandas               as pd
from genre_movies           import genre_movies_extraction
from genres_extraction      import genres_names_urls_extraction
from pathlib                import Path

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
    
    movies_genre={}
    for genre_name in list(genres.keys()):
        print("\n >>>>>>> Genre: " +genre_name+ " <<<<<<< \n" )
        genre_url = genres[genre_name]
        movies_genre[genre_name]= genre_movies_extraction(genre_name, genre_url, headers)
        print(f"{genre_name} movies:" + str(genre_movies_extraction(genre_name, genre_url, headers)))

    print("3. CSV data storage")
    # Data to print in CSV
    data_to_csv={}
    # Data structure to display the CSV correctly
    for _genre in movies_genre.keys():
        keys_dict = movies_genre[_genre].keys()
        for _id in keys_dict:
            data_dict = movies_genre[_genre][_id]
            for _key in data_dict:
                if data_to_csv.get(_key) is None:
                    data_to_csv[_key] = []
                data_to_csv[_key].append(str(data_dict[_key]))

    # Path to store final CSV
    p = Path(os.path.realpath(__file__))
    csv_path  = os.path.join(p.parent.parent, "dataset/data.csv")
    df = pd.DataFrame.from_dict(data_to_csv)
    df.to_csv(csv_path, encoding='utf-8', index=False)

if __name__ == "__main__":
    main()