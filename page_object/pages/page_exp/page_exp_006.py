from page_object.pages.locators import RegistrationLocators
from page_object.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class Registration(BasePage):

    def click_registration(self):
        self.search_field = self.find_element(RegistrationLocators.REGISTER_LINK)

    def location_once_scrolled(self):
        self.security_link()
        self.search_field.click()

    def enter_first_name(self, word):
        search_field = self.find_element(RegistrationLocators.FIRST_NAME_LINK)
        search_field.send_keys(word)

    def enter_second_name(self):
        search_field = self.find_element(RegistrationLocators.SECOND_NAME_LINK)
        search_field.click()

    def error_is_not_displayed(self):
        try:
            assert self.find_element(RegistrationLocators.ERROR_MESSAGE)
        except NoSuchElementException:
            return True
