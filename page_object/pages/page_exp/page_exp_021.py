from page_object.pages.locators import RegistrationLocators
from page_object.pages.base_page import BasePage


class Registration(BasePage):

    def click_registration(self):
        self.search_field = self.find_element(RegistrationLocators.REGISTER_LINK)

    def location_once_scrolled(self):
        self.security_link()
        self.search_field.click()

    def enter_password(self, word):
        search_field = self.find_element(RegistrationLocators.PASSWORD_LINK)
        search_field.send_keys(word)

    def enter_password_confirmation(self, word):
        search_field = self.find_element(RegistrationLocators.PASSWORD_CONFIRMATION)
        search_field.send_keys(word)

    def click_register_button(self):
        search_field = self.find_element(RegistrationLocators.REGISTER_BUTTON)
        search_field.click()

    def error_is_displayed(self):
        assert self.find_element(RegistrationLocators.ERROR_MESSAGE_PASSWORD)
