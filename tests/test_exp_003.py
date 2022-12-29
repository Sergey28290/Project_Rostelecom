from page_object.pages.page_exp.page_exp_003 import AutorizationPage


def test_exp_003(browser):
    reg = AutorizationPage(browser)
    reg.go_to_site()
    reg.enter_login("+71234567890")
    reg.enter_password("FDnx4937")
    reg.enter_input_button()
    reg.search_personal_account_page()
