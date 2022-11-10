"""
Description: This file contains the logic necessary to dynamically evaluate movies. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

import time
from selenium.webdriver.common.by import By

def dynamically_review_movie(driver, session, genre_name):
    """Function to dynamically rate movies
    
    Inputs:
        - driver: Input needed to manage the open browser session and 
                    to have dynamic interaction with the browser
        - session: Input is necessary to be able to match the driver's 
                    cookies with the session by using request
        - genre_name: Name of the genre in which the film will be rated
    """

    # Open the Firefox browser
    try:
        driver.find_element(By.LINK_TEXT, genre_name).click()
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "loadlate").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "sc-ab12c7bd-5.fwcHnW").click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ipc-starbar__touch").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".ipc-rating-prompt__container .ipc-rating-prompt__rating-container .ipc-rating-prompt__rate-button ").click()
        time.sleep(3)
        driver.get("https://www.imdb.com/feature/genre/?ref_=login")
    except: 
        driver.get("https://www.imdb.com/feature/genre/?ref_=login")
    
    # The same cookies are given to the requests session and the browser to have the 2 sessions open
    for cookie in driver.get_cookies():
        session.cookies.set(cookie['name'], cookie['value'])
    
    return session