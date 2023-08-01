from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


connect_button = (By.XPATH, '//a[text()="Подключиться к платформе"]')
integration_form_discr = (By.XPATH, '//div[@class="t702__descr t-descr t-descr_xs"]')
integration_form_name_field = (By.XPATH, '//input[@name="NAME"]')
integration_form_company_field = (By.XPATH, '//input[@name="COMPANY_TITLE"]')
integration_form_email_field = (By.XPATH, '//input[@name="EMAIL"]')
integration_form_phone_field = (By.XPATH, '//input[@name="PHONE"]')
integration_form_submit_button = (By.XPATH, '//div[@class="t-form__inputsbox"]/div[@class="t-form__submit"]/'
                                            'button[@class="t-submit"][1]')
integration_form_exit_button = (By.XPATH, '//div[@class="t-popup__container t-width t-width_6 t-popup__container-'
                                          'static t-popup__container-animated"]//following-sibling::'
                                          'div[@class="t-popup__close t-popup__block-close"]/button')
developers_top_button = (By.XPATH, '//a[text() = "Разработчикам"][1]')
developers_top_button_api = (By.XPATH, '//div[@class="t396__elem tn-elem tn-elem__4647465181655364989565"]/a')


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://rapporto.ru')

    def click_connect_button(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of(self.find(*connect_button)))
        self.find(*connect_button).click()

    def get_text_integration_form_discr(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of(self.find(*integration_form_discr)))
        return self.find(*integration_form_discr).text

    def filling_integration_form_field(self, name, text):
        field = (By.XPATH, f'//input[@name="{name}"]')
        self.find(*field).send_keys(text)

    def get_integration_form_field(self, name):
        field = (By.XPATH, f'//input[@name="{name}"]')
        return self.find(*field).get_attribute('value')

    def get_error_text_integration_form_field(self, name):
        return self.find(*(By.XPATH, f'//input[@name="{name}"]/following-sibling::div[@class="t-input-error"]')).text

    def click_integration_form_submit_button(self):
        self.find(*integration_form_submit_button).click()

    def click_integration_form_exit(self):
        self.find(*integration_form_exit_button).click()

    def move_to_developers_top_button(self, driver):
        ActionChains(driver).move_to_element(self.find(*developers_top_button)).perform()

    def click_developers_top_button_api(self):
        self.find(*developers_top_button_api).click()
