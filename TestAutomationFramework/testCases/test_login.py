
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class TestDCCMLogin:
    URL = "https://login.microsoftonline.com/"
    username = os.getenv("DCCM_USERNAME", "Olalekan.Adebule@ukhotest1.onmicrosoft.com")
    password = os.getenv("DCCM_PASSWORD", "Update123")

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()

    #Clear all cookies from the browser
    def clear_cookies(self):
            self.driver.delete_all_cookies()
            print("Cookies cleared successfully.")

    def test_home(self):
        self.driver.get(self.URL)  # Open the URL
        time.sleep(2)

        # Click on the "Other account" tile
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "otherTileText"))
        ).click()
        time.sleep(2)

        # Wait for and fill in the username field
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "i0116"))
        )
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(2)

        # Click the "Next" button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        ).click()
        time.sleep(2)

        # Wait for and fill in the password field
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "i0118"))
        )
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(2)

        # Click the "Sign in" button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        ).click()
        time.sleep(2)

        # Click the "Next" button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        ).click()
        time.sleep(2)

        self.driver.get("https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdccm-ukhotest1-perf."
                        "crm11.dynamics.com%2F&data=05%7C02%7CSivaram.Kasina%40homeoffice.gov.uk%7Ca49c3505694046f"
                        "072d808dcfa8d3c53%7Cf24d93ecb2914192a08af182245945c2%7C0%7C0%7C638660731709725138%7CUn"
                        "known%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6"
                        "Mn0%3D%7C0%7C%7C%7C&sdata=r745f3HjzkNLOgIci6jgyScwkwS%2FcHTslBpu4HC%2FpLA%3D&reserved=0")

        # Wait for the title to contain "Power Apps"
        WebDriverWait(self.driver, 500).until(
            EC.title_contains("Power Apps")
        )
        time.sleep(5)
        # Capture the actual title
        act_title = self.driver.title

        # Print the actual title for debugging
        print(f"Verified title: {act_title}")

        # Assert that the title contains "Power Apps"
        assert "Power Apps" in act_title, f"Expected title to contain 'Power Apps' but got '{act_title}'"

        # Print a success message
        print("Power App login is successful!")

        # Wait for 20 seconds before closing the page
        time.sleep(20)

        # Close the browser
        self.driver.quit()



