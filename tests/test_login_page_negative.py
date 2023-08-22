import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("studentWrong", "Password123", "Your username is invalid!"),
                              ("student", "Password", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):

        logging_page = LoginPage(driver)
        logging_page.open()
        logging_page.execute_login(username, password)
        assert logging_page.get_error_message() == expected_error_message, "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_username(self, driver):
        url = "https://practicetestautomation.com/practice-test-login/"

        driver.get(url)

        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.ID, "password")
        submit_btn_locator = driver.find_element(By.ID, "submit")

        username_locator.send_keys("studentWrong")
        password_locator.send_keys("Password123")
        submit_btn_locator.click()

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"
        time.sleep(4)

        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

        driver.close()

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_password(self, driver):
        url = "https://practicetestautomation.com/practice-test-login/"

        driver.get(url)

        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.ID, "password")
        submit_btn_locator = driver.find_element(By.ID, "submit")

        username_locator.send_keys("student")
        password_locator.send_keys("Password")
        submit_btn_locator.click()

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"
        time.sleep(4)

        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"

        driver.close()
