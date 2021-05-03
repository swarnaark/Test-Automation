from selenium.webdriver.common.by import By


class shopping_cart():
    def __init__(self, driver):
        self.driver = driver

    click_cart = (By.CLASS_NAME, "shopping_cart_link")
    item_cart_1 = (By.ID, "item_5_title_link")
    item_cart_2 = (By.ID, "item_4_title_link")
    click_checkout_button = (By.ID, "checkout")

    def click_cart_button(self):
        return self.driver.find_element(*shopping_cart.click_cart)

    def check_item1(self):
        return self.driver.find_element(*shopping_cart.item_cart_1)

    def check_item2(self):
        return self.driver.find_element(*shopping_cart.item_cart_2)

    def click_checkout(self):
        return self.driver.find_element(*shopping_cart.click_checkout_button)
