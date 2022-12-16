from helpers.support_functions import *

not_found_info = '/html/body/h1'


def not_found_message_visible(drver_instance):
    wait_for_visibility_of_element_xpath(drver_instance, not_found_info)
    elem = drver_instance.find_element_by_xpath(not_found_info)
    return elem.is_displayed()
