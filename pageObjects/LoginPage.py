from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_textbox = (By.NAME, "user-name")
    password_textbox = (By.NAME, "password")
    submit_button = (By.ID, "login-button")
    error_message = (By.TAG_NAME, "h3")

    def login_username(self):
        return self.driver.find_element(*LoginPage.username_textbox)

    def login_password(self):
        return self.driver.find_element(*LoginPage.password_textbox)

    def submit(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def error(self):
        return self.driver.find_element(*LoginPage.error_message)







