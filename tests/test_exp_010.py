from page_object.pages.page_exp.page_exp_010 import Registration


def test_exp_010(browser):
    reg = Registration(browser)
    reg.go_to_site()
    reg.click_registration()
    reg.location_once_scrolled()
    reg.enter_second_name("Иввввввввввввввввввввввввввввв ")
    reg.enter_first_name()
    reg.error_is_not_displayed()
