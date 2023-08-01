from pages.main_page import MainPage


def test_click_connect_button(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_connect_button(driver)
    assert main_page.get_text_integration_form_discr(driver) == 'Заполните короткую форму'


def test_error_text_name_field(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_connect_button(driver)
    main_page.click_integration_form_submit_button()
    assert main_page.get_error_text_integration_form_field('NAME') == 'Обязательное поле'
    main_page.click_integration_form_submit_button()
    assert main_page.get_error_text_integration_form_field('NAME') == 'Пожалуйста, заполните все обязательные поля'


def test_error_text_email_field(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_connect_button(driver)
    main_page.click_integration_form_submit_button()
    assert main_page.get_error_text_integration_form_field('EMAIL') == 'Пожалуйста, заполните все обязательные поля'


def test_save_integration_form_fields(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_connect_button(driver)
    main_page.filling_integration_form_field('NAME', 'name')
    main_page.filling_integration_form_field('COMPANY_TITLE', 'company_title')
    main_page.filling_integration_form_field('EMAIL', 'email')
    main_page.filling_integration_form_field('PHONE', 'phone')
    main_page.click_integration_form_exit()
    main_page.click_connect_button(driver)
    assert main_page.get_integration_form_field('NAME') == 'name' and \
           main_page.get_integration_form_field('COMPANY_TITLE') == 'company_title' and \
           main_page.get_integration_form_field('EMAIL') == 'email' and \
           main_page.get_integration_form_field('PHONE') == 'phone'


def test_mod(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.move_to_developers_top_button(driver)
    main_page.click_developers_top_button_api()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert driver.current_url == 'https://docs.rapporto.ru/display/docsAPI'
