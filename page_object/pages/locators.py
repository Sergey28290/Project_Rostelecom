from selenium.webdriver.common.by import By


class RegistrationLocators:
    REGISTER_LINK = (By.XPATH, "//*[@id='kc-register']")
    FIRST_NAME_LINK = (By.XPATH, "//*[@name='firstName']")
    SECOND_NAME_LINK = (By.XPATH, "//*[@name='lastName']")
    LOGIN_DETAILS_LINK = (By.XPATH, "//*[@id='address']")
    PASSWORD_LINK = (By.XPATH, "//*[@id='password']")
    PASSWORD_CONFIRMATION = (By.XPATH, "//*[@id='password-confirm']")
    REGISTER_BUTTON = (By.XPATH, "//*[@name='register']")
    EMAIL_CONFIRMATION = (By.XPATH, "//*[contains(text(),'Подтверждение email')]")
    TELEPHONE_CONFIRMATION = (By.XPATH, "//*[contains(text(),'Подтверждение телефона')]")
    LOGIN_LINK = (By.XPATH, "//input[@id='username']")
    PASSWORD_AUTORIZATION = (By.XPATH, "//*[@id='password']")
    INPUT_BUTTON_LINK = (By.XPATH, "//*[@id='kc-login']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//*[@class='user-name__last-name']")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(),'Необходимо заполнить поле кириллицей')]")
    ERROR_MESSAGE_PASSWORD = (By.XPATH, "//*[contains(text(),'Пароли не совпадают')]")