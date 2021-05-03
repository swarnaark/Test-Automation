from selenium.webdriver.common.by import By


class order_complete():
    def __init__(self, driver):
        self.driver = driver

    order_finish = (By.ID, "finish")

    def orderconfirmation_page(self):
        return self.driver.find_element(*order_complete.order_finish)