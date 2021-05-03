# Testing the Login of an application as Locked_out user
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import baseclass


class TestLogin(baseclass):
    def test_locked_out_user(self):
        loginpage = LoginPage(self.driver)
        loginpage.login_username().send_keys("locked_out_user")
        loginpage.login_password().send_keys("secret_sauce")
        loginpage.submit().click()
        message = loginpage.error().text
        assert "Epic sadface: Sorry, this user has been locked out." == message
        self.driver.get_screenshot_as_file("login screen locked error.png")
