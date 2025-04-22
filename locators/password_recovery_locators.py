from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'
    input_email = (By.CLASS_NAME, 'input__textfield')
    button_recover = (By.CLASS_NAME, 'button_button__33qZ0')
    input_password = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    eye_icon = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    value_password_is_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')
    value_password_is_invisible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                             '"input_type_password")]')
