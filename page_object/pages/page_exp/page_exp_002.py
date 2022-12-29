from page_object.pages.locators import RegistrationLocators
from page_object.pages.base_page import BasePage
from allure_commons.types import AttachmentType
import allure


class RegistrationTelephone(BasePage):

    def click_registration(self):
        with allure.step('Нажата кнопка "Зарегистрироваться"'):
            pass
        self.search_field = self.find_element(RegistrationLocators.REGISTER_LINK)

    def location_once_scrolled(self):
        self.security_link()
        self.search_field.click()
        with allure.step('Переход на страницу "Регистрация"'):
            pass

    def enter_first_name(self, word):
        search_field = self.find_element(RegistrationLocators.FIRST_NAME_LINK)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Имя"'):
            pass

    def enter_second_name(self, word):
        search_field = self.find_element(RegistrationLocators.SECOND_NAME_LINK)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Фамилия"'):
            pass

    def enter_login_details(self, word):
        search_field = self.find_element(RegistrationLocators.LOGIN_DETAILS_LINK)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Данные для входа"'):
            pass

    def enter_password(self, word):
        search_field = self.find_element(RegistrationLocators.PASSWORD_LINK)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Пароль"'):
            pass

    def enter_password_confirmation(self, word):
        search_field = self.find_element(RegistrationLocators.PASSWORD_CONFIRMATION)
        search_field.send_keys(word)
        with allure.step('Введено значение в поле "Подтверждение пароля"'):
            pass

    def click_register_button(self):
        search_field = self.find_element(RegistrationLocators.REGISTER_BUTTON)
        search_field.click()
        with allure.step('Нажата кнопка "Зарегистрироваться"'):
            pass

    def search_telephone_confirmation(self):
        assert self.find_element(RegistrationLocators.TELEPHONE_CONFIRMATION)
        with allure.step('Успешный переход на страницу "Подтверждение телефона"'):
            pass
        with allure.step("Cоздание скриншота страницы"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)