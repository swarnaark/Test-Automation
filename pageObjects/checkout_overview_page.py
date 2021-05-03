from selenium.webdriver.common.by import By


class checkout_overview():
    def __init__(self, driver):
        self.driver = driver

    payment_details = (By.CSS_SELECTOR,"div[class='summary_value_label']")
    shipment_details = (By.XPATH,"//div[text()='FREE PONY EXPRESS DELIVERY!']" )
    total_value = (By.CLASS_NAME, "summary_total_label")

    def payment(self):
        return self.driver.find_element(*checkout_overview.payment_details)

    def shipment(self):
        return self.driver.find_element(*checkout_overview.shipment_details)

    def total(self):
        return self.driver.find_element(*checkout_overview.total_value)
