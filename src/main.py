"""
Description:


Authors: 
    Lucas Gómez, Joan Amengual
"""

from genre_movies import genre_movies_extraction

def main():

    print("1. URL genre extraction: https://www.imdb.com/feature/genre/?ref_=nv_ch_gr")

    print("2. Extraction of information from movies of each genre")
    genre_name = 'comedy'
    genre_url = "https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=MCMWMC4F4V3YRQFB7292&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1"
    print(genre_movies_extraction(genre_name, genre_url))

    print("3. Extraction of information from a movie")


if __name__ == "__main__":
    main()