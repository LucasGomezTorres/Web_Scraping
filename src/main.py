"""
Description:


Authors: 
    Lucas Gómez, Joan Amengual
"""

from genre_movies import genre_movies_extraction

from genres_extraction import genres_names_urls_extraction

def main():

    print("1. URL and names genres extraction:")
    genres_url = "https://www.imdb.com/feature/genre"

    print("Genres:" + str(genres_names_urls_extraction(genres_url)[0]))
    print("\n")
    print("URLs:" + str(genres_names_urls_extraction(genres_url)[1]))

    print("2. Extraction of information from movies of each genre")
    print("\n")
    genre_name = 'comedy'
    genre_url = "https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=MCMWMC4F4V3YRQFB7292&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1"
    print(genre_movies_extraction(genre_name, genre_url))

    print("\n")
    print("3. Extraction of information from a movie")


if __name__ == "__main__":
    main()