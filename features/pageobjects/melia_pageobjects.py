# -*- coding: utf-8 -*-
u"""
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MeliaPageObject:
    """class - Initial landing page
    """

    cookies_locator = (By.XPATH, '//*[@id="didomi-notice-agree-button"]/span')
    destination_locator = (By.ID, 'mbe-destination-input')
    default_destination_locator = (By.XPATH, "//div[@id='too-be']/div/div[2]/div/div/div[2]/ul[2]/li[2]/b")
    dates_locator = (By.XPATH, '//*[@id="mbe-dates-select"]/span[1]')
    base_time_locator = (By.CSS_SELECTOR, 'li.dYEAR-MONTH-DAY span')
    accept_button_persons_locator = (By.CSS_SELECTOR, 'button.mbe-btn')
    search_button_locator = (By.ID, 'mbe-search-button')
    dialog_hotels_search_locator = (By.XPATH, '//*[@id="titHotelesDisp"]')

    uniqued_xpath = (By.XPATH, "//*[@class='c-hotel-sheet-room__content-room']")

    def __init__(self, driver):
        self.driver = driver


    def loaded(self):
        """
        """
        found_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.dialog_hotels_search_locator))

        return True if 'HOTEL' in found_element.text else False


    def goto_search_and_write(self, destination):
        
        cookies_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.cookies_locator))
        cookies_element.click()
        
        destination_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.destination_locator))
        destination_element.click()

        self.driver.implicitly_wait(1)

        destination_element.send_keys(destination)

        default_destination_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.default_destination_locator))
        default_destination_element.click()

        return self


    def goto_dates_and_select(self, date):

        day, month, year = date.split('/')[0], date.split('/')[1], date.split('/')[2]

        new_base_time_locator_firt = (self.base_time_locator[0], self.base_time_locator[1].replace('YEAR', year).replace('MONTH', month).replace('DAY', day))
        new_base_time_locator_second = (self.base_time_locator[0], self.base_time_locator[1].replace('YEAR', year).replace('MONTH', month).replace('DAY', str(int(day)+5)))

        firts_time_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(new_base_time_locator_firt))
        firts_time_element.click()

        self.driver.implicitly_wait(3)

        second_time_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(new_base_time_locator_second))
        second_time_element.click()

        return self

    def select_persons_and_search(self):

        accept_button_persons_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.accept_button_persons_locator))
        accept_button_persons_element.click()
        
        search_button_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.search_button_locator))
        search_button_element.click()

        return self

    def get_all_rooms(self):
        """
        """
        cookies_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.cookies_locator))
        cookies_element.click()

        found_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.uniqued_xpath))

        numbers_of_hotels_in_web = f'\n\tThere are {len(found_element)} rooms available on the website'

        return numbers_of_hotels_in_web