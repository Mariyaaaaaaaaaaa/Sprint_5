import random
from exrex import getone as get

from locators import Locators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

random_name = get(r'[aeiouy][a-z]{5}')


""" Успешная регистрация """
def test_registration_success(driver):
    driver.get(Locators.page_register_url)
    driver.find_element(By.XPATH, Locators.name_auth).send_keys(random_name)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(f'{random_name}@mail.ru')
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys(f'{random.randint(100000, 9999999)}')
    driver.find_element(By.XPATH, Locators.button_auth).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    assert driver.current_url == Locators.page_login_url


""" Регистрация - ошибка для некорректного пароля """
def test_registration_incorrect_password(driver):
    driver.get(Locators.page_register_url)
    driver.find_element(By.XPATH, Locators.name_auth).send_keys(Locators.user_name)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys('12345')
    driver.find_element(By.XPATH, Locators.button_auth).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.incorrect_password_text)))
    assert driver.find_element(By.XPATH, Locators.incorrect_password_text).text == "Некорректный пароль"


""" Регистрация существующего пользователя  """
def test_registration_existing_user(driver):
    driver.get(Locators.page_register_url)
    driver.find_element(By.XPATH, Locators.name_auth).send_keys(Locators.user_name)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.button_auth).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.text_user_is_exists)))
    assert driver.find_element(By.XPATH, Locators.text_user_is_exists).text == "Такой пользователь уже существует"


""" Регистрация с пустым полем "Имя" """
def test_registration_no_name(driver):
    driver.get(Locators.page_register_url)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(f'{random_name}@mail.ru')
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys(f'{random.randint(100000, 9999999)}')
    driver.find_element(By.XPATH, Locators.button_auth).click()
    WebDriverWait(driver, 50)
    assert driver.current_url == Locators.page_register_url


""" Вход по кнопке «Войти в аккаунт» на главной странице """
def test_login_in_main_page(driver):
    driver.get(Locators.main_page_url)
    driver.find_element(By.XPATH, Locators.button_login_to_account_main).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == Locators.main_page_url


""" Вход через кнопку "Личный кабинет"  """
def test_login_in_personal_account(driver):
    driver.get(Locators.main_page_url)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == Locators.main_page_url


""" Вход через кнопку в форме регистрации  """
def test_login_in_registration_form(driver):
    driver.get(Locators.page_register_url)
    driver.find_element(By.XPATH, Locators.button_log_in_reg_form).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == Locators.main_page_url


""" Вход через кнопку в форме восстановления пароля  """
def test_login_in_restore_password(driver):
    driver.get(Locators.main_page_url)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, Locators.button_restore_password).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Восстановление пароля"]')))
    driver.find_element(By.XPATH, Locators.button_log_in_restore_password).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == Locators.main_page_url


""" Переход из личного кабинета в конструктор  """
def test_go_to_constructor_from_personal_account(driver):
    driver.get(Locators.page_login_url)
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    driver.find_element(By.XPATH, './/p[text()="Конструктор"]').click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == Locators.main_page_url


""" Переход из личного кабинета на логотип Stellar Burgers """
def test_go_to_logo_from_personal_account(driver):
    driver.get(Locators.page_login_url)
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    driver.find_element(By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]').click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    assert driver.current_url == Locators.main_page_url


""" Выход из аккаунта по кнопке "Выйти" в личном кабинете  """
def test_exit_in_personal_account(driver):
    driver.get(Locators.main_page_url)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]')))
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    driver.find_element(By.XPATH, Locators.button_exit_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/h2[text()="Вход"]')))
    assert driver.current_url == Locators.page_login_url


"""  Переход по разделам (Начинки) """
def test_switch_to_section_fillings(driver):
    driver.get(Locators.main_page_url)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')))
    driver.find_element(By.XPATH,'.//span[text() = "Начинки"]').click()
    assert 'tab_tab_type_current' in driver.find_element(By.XPATH,'.//span[text() = "Начинки"]/parent::div').get_attribute("class")


"""  Переход по разделам (Соусы) """
def test_switch_to_section_sauces(driver):
    driver.get(Locators.main_page_url)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')))
    driver.find_element(By.XPATH,'.//span[text() = "Соусы"]').click()
    assert 'tab_tab_type_current' in driver.find_element(By.XPATH,'.//span[text() = "Соусы"]/parent::div').get_attribute("class")


"""  Переход по разделам (Булки) """
def test_switch_to_section_bun(driver):
    driver.get(Locators.main_page_url)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')))
    driver.find_element(By.XPATH, './/span[text() = "Начинки"]').click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH,'.//span[text() = "Булки"]').click()
    assert 'tab_tab_type_current' in driver.find_element(By.XPATH,'.//span[text() = "Булки"]/parent::div').get_attribute("class")
