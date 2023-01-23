from page_object.pages.page_exp.page_exp_002 import RegistrationTelephone
import allure


@allure.feature('Перенаправление пользователя на страницу Личного кабинета при успешной регистрации по телефону"')
@allure.story('Открыта страница "Авторизация"')
def test_exp_002(browser):
    reg = RegistrationTelephone(browser)
    reg.go_to_site()
    reg.click_registration()
    reg.location_once_scrolled()
    reg.enter_first_name("Иван")
    reg.enter_second_name("Иванов")
    reg.enter_login_details("+71234567845")
    reg.enter_password("password")
    reg.enter_password_confirmation("password")
    reg.click_register_button()
    reg.search_telephone_confirmation()
