from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver

    def get(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)

    def authorization(self, user_name, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()