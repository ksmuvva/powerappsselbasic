from selenium import webdriver


class Login:
    # Locators for the web elements
    textbox_username_id = "i0116"
    button_next_id = "idSIButton9"
    textbox_password_id = "i0118"
    button_signin_id = "idSIButton9"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Set username
    def set_username(self, username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    # Click next button
    def click_next(self):
        self.driver.find_element("id", self.button_next_id).click()

    # Set password
    def set_password(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    # Click sign-in button
    def click_signin(self):
        self.driver.find_element("id", self.button_signin_id).click()
