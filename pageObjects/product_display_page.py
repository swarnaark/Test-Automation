from selenium.webdriver.common.by import By


class product_display():
    def __init__(self, driver):
        self.driver = driver

    sort_filter = (By.CLASS_NAME, "product_sort_container")
    item = (By.CLASS_NAME, "inventory_item_name")
    item_price = (By.CLASS_NAME, "inventory_details_price")
    add_cart = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    back_button = (By.ID, "back-to-products")
    item1 = (By.CLASS_NAME, "inventory_item_img")
    item_price1 = (By.CLASS_NAME, "inventory_details_price")
    add_cart_item1 = (By.ID, "add-to-cart-sauce-labs-backpack")

    def sort(self):
        return self.driver.find_element(*product_display.sort_filter)

    def product_list(self):
        return self.driver.find_element(*product_display.item)

    def product_price(self):
        return self.driver.find_element(*product_display.item_price)

    def product_add(self):
        return self.driver.find_element(*product_display.add_cart)

    def back(self):
        return self.driver.find_element(*product_display.back_button)

    def product_list1(self):
        return self.driver.find_element(*product_display.item1)

    def product_price1(self):
        return self.driver.find_element(*product_display.item_price1)

    def add_cart_item(self):
        return self.driver.find_element(*product_display.add_cart_item1)



