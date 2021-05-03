from selenium.webdriver.common.by import By


class check_out_address():
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.CSS_SELECTOR, "input[name='firstName']")
    last_name = (By.CSS_SELECTOR, "input[name='lastName']")
    zip = (By.CSS_SELECTOR, "input[name='postalCode']")
    continue_button = (By.ID, "continue")

    def firstname(self):
        return self.driver.find_element(*check_out_address.first_name)

    def lastname(self):
        return self.driver.find_element(*check_out_address.last_name)

    def postal_zip(self):
        return self.driver.find_element(*check_out_address.zip)

    def click_continue(self):
        return self.driver.find_element(*check_out_address.continue_button)


