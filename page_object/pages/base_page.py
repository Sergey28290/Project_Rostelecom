from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"

    def go_to_site(self):
        self.driver.get(self.base_url)

        self.driver.implicitly_wait(10)

    def find_element(self, locator):
        self.element = self.driver.find_element(*locator)
        return self.element

    def security_link(self):
        _ = self.element.location_once_scrolled_into_view
