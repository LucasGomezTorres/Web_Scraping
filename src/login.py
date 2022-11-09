"""
Description: This file contains the logic necessary to login in the page and create a session with the credentials. 

Authors: 
    Lucas Gómez, Joan Amengual
"""

import requests
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

def login(url_login, data_login, headers):
    """
    Function that creates and return a session with the credentials and it will be used to access the data from the requests library 
    and through the Firefox browser via Selenium.

    Inputs:
        - url_login: url to login in the page to extract information.
        - data_login: data to login in the page.
        - headers: information for modifying the user-agent.
    """

    # Open the Firefox browser
    driver = Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url_login)

    # The session is created with requests
    session = requests.Session()

    # Cookies generated by the browser are passed to the requests session
    for cookie in driver.get_cookies():
        session.cookies.set(cookie["name"], cookie["value"])

    # The login with the user data
    response = session.post(url_login, data=data_login, headers=headers)

    # It checks if the server gives any error
    if response.status_code == 400 or response.status_code == 401:
            print("Error de petición")

    # We export the response cookies to the browser
    resp_cookies_dict = response.cookies.get_dict()
    response_cookies_browser = [{'name':name, 'value':value} for name,value in resp_cookies_dict.items()]
    for c in response_cookies_browser:
        driver.add_cookie(c)

    # The browser now contains the authentication cookies   
    driver.get(url_login)

    # The same cookies are given to the requests session and the browser to have the 2 sessions open
    for cookie in driver.get_cookies():
        session.cookies.set(cookie['name'], cookie['value'])

    return session


