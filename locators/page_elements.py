""" PYTEST PAGE ELEMENT IDENTIFIERS GO HERE """

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USN_INPUT = (By.XPATH, 'sample_xpath')
    PWD_INPUT = (By.XPATH, 'sample_xpath')
    LOGIN_CTA = (By.XPATH, 'sample_xpath')


class LandingPageLocators(object):
    SEARCH_CTA = (By.XPATH, 'sample_xpath')

class Search(object):
   SEARCH_FIELD = (By.XPATH, '//input[@title="Search"]')
   SEARCH_CTA = (By.XPATH, '(//input[@value="Google Search"])[2]')

   # EMAIL = (By.ID, 'email')
   # PW = (By.ID, 'pass')
   # LOGIN = (By.XPATH, "//label[@id='loginbutton']")