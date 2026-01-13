from selenium.webdriver.common.by import By

class AccountPageLocators:
    profile = (By.XPATH, '//a[@href = "/account/profile"]')
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')
    button_logout = (By.XPATH, '//button[@type = "button"]')
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'
    description_of_section = (By.XPATH, '//p[contains(@class, "Account_text")]')
