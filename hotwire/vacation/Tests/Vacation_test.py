from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from Utilities.date_utility import DateGet
from Base.selenium_driver import SeleniumWebdriver


class Vacation(unittest.TestCase):
    def test_vacation(self):
        driver = webdriver.Chrome()
        baseUrl="https://www.hotwire.com/"
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)


        vacation_tab=driver.find_element_by_xpath('//header[@id="header"]//a[text()="Vacations"]')
        vacation_tab.click()
        time.sleep(5)

        flight_tab=driver.find_element_by_xpath("//div[contains(@class,'hw-btn')]//button[1]")
        if not flight_tab.is_selected():
            flight_tab.click()
        else:
            print("already selected")

        hotel_tab=driver.find_element_by_xpath("//div[contains(@class,'hw-btn')]//button[2]")
        if not hotel_tab.is_selected():
            hotel_tab.click()
        else:
            print("already selected")


        car_tab= driver.find_element_by_xpath("//div[contains(@class,'hw-btn')]//button[3]")
        if not car_tab.is_selected():
            car_tab.click()
        else:
            print("already selected")

        fly_from_field=driver.find_element_by_css_selector("#farefinder-package-origin-location-input")
        c1=fly_from_field.send_keys("SFO")


        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.move_to_element(fly_from_field).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            sfo_element = driver.find_element_by_xpath(
                "//*[contains(@class,'uib-typeahead-match')]//a[contains(@title,'San')]")
            actions.move_to_element(sfo_element).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")


        fly_to_field=driver.find_element_by_css_selector("#farefinder-package-destination-location-input")
        c2 =fly_to_field.send_keys("LAX")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.move_to_element(fly_to_field).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            lax_element = driver.find_element_by_xpath(
                "//*[contains(@class,'uib-typeahead-match')]//a[contains(@title,'Los')]")
            actions.move_to_element(lax_element).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")
        time.sleep(5)
        #Start date
        d_date=driver.find_element_by_id("farefinder-package-startdate-input")
        d_date.clear()
        d1 =DateGet.start_day(self)
        d_date.send_keys(d1)
        time.sleep(5)
        #return date
        r_date=driver.find_element_by_id("farefinder-package-enddate-input")
        r_date.clear()
        d2 =DateGet.return_day(self)
        r_date.send_keys(d2)
        time.sleep(5)

        pickup = driver.find_element_by_xpath('//select[@id="farefinder-package-pickuptime-input"]')
        pickup.click()
        sel = Select(pickup)
        sel.select_by_index("2")
        time.sleep(2)


        drop = driver.find_element_by_xpath('//select[@id="farefinder-package-dropofftime-input"]')
        drop.click()
        sel1 =Select(drop)
        sel1.select_by_index("0")
        time.sleep(2)

        find_deal_button=driver.find_element_by_id("farefinder-package-search-button")
        find_deal_button.click()

        time.sleep(15)

        element_locator=driver.find_element_by_xpath("//header[@id='hotelResultTitle']/h1[contains(text(),Start)]")
        text=element_locator.text
        print(text)

        self.assertEqual(text,"Start by choosing your hotel",msg="Element found")


if __name__ =='__main__':
    unittest.main(verbosity=2)

# aa = VacationTest()
# aa.Test_vacation()

