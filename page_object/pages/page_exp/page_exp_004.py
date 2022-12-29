from page_object.pages.locators import RegistrationLocators
from page_object.pages.base_page import BasePage
from allure_commons.types import AttachmentType
import allure


class AutorizationPage(BasePage):

    def enter_login(self, word):
        search_field = self.find_element(RegistrationLocators.LOGIN_LINK)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Почта"'):
            pass

    def enter_password(self, word):
        search_field = self.find_element(RegistrationLocators.PASSWORD_AUTORIZATION)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Пароль"'):
            pass

    def enter_input_button(self):
        search_field = self.find_element(RegistrationLocators.INPUT_BUTTON_LINK)
        search_field.click()
        with allure.step('Нажата кнопка "Войти"'):
            pass

    def search_personal_account_page(self):
        assert self.find_element(RegistrationLocators.PERSONAL_ACCOUNT_LINK)
        with allure.step('Успешный переход на страницу "Личный кабинет"'):
            pass
        with allure.step("Cоздание скриншота страницы"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
