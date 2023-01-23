from page_object.pages.page_exp.page_exp_004 import AutorizationPage


def test_exp_004(browser):
    reg = AutorizationPage(browser)
    reg.go_to_site()
    reg.enter_login("gmail@gmail.com")
    reg.enter_password("password")
    reg.enter_input_button()
    reg.search_personal_account_page()
