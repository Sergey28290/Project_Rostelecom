from page_object.pages.locators import RegistrationLocators
from page_object.pages.base_page import BasePage
from allure_commons.types import AttachmentType


class AutorizationPage(BasePage):

    def enter_login(self, word):
        search_field = self.find_element(RegistrationLocators.LOGIN_LINK)
        search_field.send_keys(word)

    def enter_password(self, word):
        search_field = self.find_element(RegistrationLocators.PASSWORD_AUTORIZATION)
        search_field.send_keys(word)

    def enter_input_button(self):
        search_field = self.find_element(RegistrationLocators.INPUT_BUTTON_LINK)
        search_field.click()

    def search_personal_account_page(self):
        assert self.find_element(RegistrationLocators.PERSONAL_ACCOUNT_LINK)
