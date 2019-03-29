from selenium.webdriver.common.by import By
from Base.selenium_driver import SeleniumWebdriver

class VacationPage():

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _vacation_tab = '//header[@id="header"]//a[text()="Vacations"]'
    _flight_tab = "//div[contains(@class,'hw-btn')]//button[1]"
    _hotel_tab = "//div[contains(@class,'hw-btn')]//button[2]"
    _car_tab = "//div[contains(@class,'hw-btn')]//button[3]"
    _fly_from_field = "#farefinder-package-origin-location-input"
    _sfo_element = "//*[contains(@class,'uib-typeahead-match')]//a[contains(@title,'San')]"
    _fly_to_field = "#farefinder-package-destination-location-input"
    _lax_element = "//*[contains(@class,'uib-typeahead-match')]//a[contains(@title,'Los')]"
    _d_date = "farefinder-package-startdate-input"
    _r_date = "farefinder-package-enddate-input"
    _pickup = '//select[@id="farefinder-package-pickuptime-input"]'
    _drop = '//select[@id="farefinder-package-dropofftime-input"]'
    _find_deal_button = "farefinder-package-search-button"

    def get_vacation_tab(self):
        return self.driver.find_element_by_xpath(self._vacation_tab)

    def get_flight_tab(self):
        return self.driver.find_element_by_xpath(self._flight_tab)

    def get_hotel_tab(self):
        return self.driver.find_element_by_xpath(self._hotel_tab)

    def get_car_tab(self):
        return self.driver.find_element_by_xpath(self._car_tab)

    def get_fly_from_field(self):
        return self.driver.find_element_by_css_selector(self._fly_from_field)

    def get_sfo_element(self):
        return self.driver.find_element_by_xpath(self._sfo_element)

    def get_fly_to_field(self):
        return self.driver.find_element_by_css_selector(self._fly_to_field)

    def get_lax_element(self):
        return self.driver.find_element_by_xpath(self._lax_element)

    def get_d_date(self):
        return self.driver.find_element_by_id(self._d_date)

    def get_r_date(self):
        return self.driver.find_element_by_id(self._r_date)

    def get_pickup(self):
        return self.driver.find_element_by_xpath(self._pickup)

    def get_drop(self):
        return self.driver.find_element_by_xpath(self._drop)

    def get_find_deal_button(self):
        return self.driver.find_element_by_id(self._find_deal_button)


    def vacation_tab_click(self):
        self.get_vacation_tab().click()

    def fight_tab_check(self):
        if not self.get_flight_tab().is_selected():
            self.get_flight_tab().click()

    def hotel_tab_check(self):
        if not self.get_hotel_tab().is_selected():
            self.get_hotel_tab().click()

    def car_tab_check(self):
        if not self.get_car_tab().is_selected():
            self.get_car_tab().click()









