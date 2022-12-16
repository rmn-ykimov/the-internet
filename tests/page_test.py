import unittest

from selenium import webdriver

from config.capabilities import chrome
from config.test_settings import TestSettings
from page_objects import auth_confirm_page, basic_auth_page, \
    file_upload_page, hovers_page, main_page, \
    not_found_page, upload_confirmation_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            desired_capabilities=chrome)
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Main Page Test
    def test_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    # Basic Auth Page Test
    def test_basic_auth_send_correct_keys(self):
        basic_auth_page.send_correct_keys(self.driver)
        self.assertTrue(auth_confirm_page.message_content_visible(self.driver))

    # Hovers page Tests
    def test_hovers_content_visible(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_visible(self.driver))

    def test_hovers_user_one(self):
        Tests.test_hovers_content_visible(self)
        hovers_page.hover_over_element_one_and_click(self.driver)
        self.assertTrue(not_found_page.not_found_message_visible(self.driver))

    def test_hovers_user_two(self):
        Tests.test_hovers_content_visible(self)
        hovers_page.hover_over_element_two_and_click(self.driver)
        self.assertTrue(not_found_page.not_found_message_visible(self.driver))

    # File Upload Page Tests
    def test_upload_file(self):
        file_upload_page.click_file_upload_tab(self.driver)
        self.assertTrue(
            file_upload_page.file_upload_content_visible(self.driver))
        file_upload_page.choose_file(self.driver)

    def test_upload_file_confirmation(self):
        Tests.test_upload_file(self)
        upload_confirmation_page.file_uploaded_msg_visible(self.driver)


if __name__ == '__main__':
    unittest.main()
