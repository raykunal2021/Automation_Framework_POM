import allure
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        login=LoginPage(driver)
        login.enter_usrname(utils.USERNAME)
        login.enter_psw(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver=self.driver
            homepage=HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x=driver.title
            assert x=="abc"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("There was an exception !!!!!")
        else:
            print("No exceptions occurred")
        finally:
            print("This block will (lw(ys execute | Close DB")



