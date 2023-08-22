import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfully
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        logging_page = LoginPage(driver)

        logging_page.open()
        logging_page.execute_login("student","Password123")
        logged_in_page = LoggedInSuccessfully(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.is_logout_btn_displayed(), "Logout button should be visible"
