from page_object.pages.page_exp.page_exp_021 import Registration


def test_exp_021(browser):
    reg = Registration(browser)
    reg.go_to_site()
    reg.click_registration()
    reg.location_once_scrolled()
    reg.enter_password("FDnx4937")
    reg.enter_password_confirmation("FDnx49370")
    reg.click_register_button()
    reg.error_is_displayed()