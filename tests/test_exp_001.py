from page_object.pages.page_exp.page_exp_001 import RegistrationEmail
import allure

@allure.feature('Перенаправление пользователя на страницу Личного кабинета при успешной регистрации по почте"')
@allure.story('Открыта страница "Авторизация"')
def test_exp_001(browser):
    reg = RegistrationEmail(browser)
    reg.go_to_site()
    reg.click_registration()
    reg.location_once_scrolled()
    reg.enter_first_name("Иван")
    reg.enter_second_name("Иванов")
    reg.enter_login_details("1a@yandex.ru")
    reg.enter_password("password")
    reg.enter_password_confirmation("password")
    reg.click_register_button()
    reg.search_email_confirmation()
