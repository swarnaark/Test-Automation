import time
# from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import LoginPage
from pageObjects.checkout_address_page import check_out_address
from pageObjects.checkout_overview_page import checkout_overview
from pageObjects.orderconfirmation_page import order_complete
from pageObjects.product_display_page import product_display
from pageObjects.shoppingcart_page import shopping_cart
from utilities.BaseClass import baseclass


class TestCheckout(baseclass):
    def test_checkout(self):
        # Login functionality
        loginpage = LoginPage(self.driver)
        loginpage.login_username().send_keys("standard_user")
        loginpage.login_password().send_keys("secret_sauce")
        loginpage.submit().click()
        time.sleep(3)
        # Sort the Items using the Price filter (Highest to Lowest)
        products = product_display(self.driver)
        dropdown = Select(products.sort())
        dropdown.select_by_value("hilo")

        # check price of jackets and backpack and add to cart

        products.product_list().click()
        jacket_price = (products.product_price())
        if jacket_price.is_displayed():
            print("Sauce Labs Fleece Jacket is 49.99 dollars")
        else:
            print("price is not visible")
        products.product_add().click()
        products.back().click()
        products.product_list1().click()
        backpack = products.product_price1()
        if backpack.is_displayed():
            print("Sauce Labs Backpack” is 29 dollars")
        else:
            print("price is not visible")
        products.add_cart_item().click()

        # assert “Sauce labs fleece jacket” & "Sauce Labs Backpack”is added to the cart

        shopping_list = shopping_cart(self.driver)
        shopping_list.click_cart_button().click()
        item1 = shopping_list.check_item1().text
        assert 'Sauce Labs Fleece Jacket' in item1
        item2 = shopping_list.check_item2().text
        assert 'Sauce Labs Backpack' in item2
        shopping_list.click_checkout().click()

        # Input details in checkout address page
        enter_details = check_out_address(self.driver)
        enter_details.firstname().send_keys("swarnaa")
        enter_details.lastname().send_keys("shree")
        enter_details.postal_zip().send_keys("0176")
        enter_details.click_continue().click()

        # assert payment/shipment info checkout overview
        complete_checkout = checkout_overview(self.driver)
        payment_info = complete_checkout.payment().text
        assert 'SauceCard #31337' in payment_info
        shipment_info = complete_checkout.shipment().text
        assert 'FREE PONY EXPRESS DELIVERY!' in shipment_info
        total = complete_checkout.total().text
        assert '86.38' in total

        # finish transaction
        finish = order_complete(self.driver)
        finish.orderconfirmation_page().click()
        print("Transaction completed successfully")
        self.driver.get_screenshot_as_file("screen complete.png")
