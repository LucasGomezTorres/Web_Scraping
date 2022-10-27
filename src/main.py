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
    print("\n")

    print("2. Extraction of information from movies of each genre")
    print("\n")
    genre_name = 'comedy'
    genre_url = "https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=MCMWMC4F4V3YRQFB7292&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1"
    print(genre_movies_extraction(genre_name, genre_url))

    print("\n")
    print("3. Extraction of information from a movie")


if __name__ == "__main__":
    main()