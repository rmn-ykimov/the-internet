from helpers.support_functions import *

basic_auth_tab = '//*[id="content"]/ul/li[3]/a'


def click_basic_auth_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, basic_auth_tab)
    elem = driver_instance.find_elem_by_xpath(basic_auth_tab)
    elem.click()


def send_correct_keys(driver_instance):
    driver_instance.get("https://admin:admin@the-internet.herokuapp.com"
                        "/basic_auth")
