import random
from exrex import getone as get

from locators import Locators
from urls import Urls

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

random_name = get(r'[aeiouy][a-z]{5}')


def set_auth_name_and_email(driver):
    driver.find_element(By.XPATH, Locators.name_auth).send_keys(Locators.user_name)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(Locators.user_email)

def set_log_in(driver):
    driver.find_element(By.XPATH, Locators.field_email_xpath).send_keys(Locators.user_email)
    driver.find_element(By.XPATH, Locators.field_password_xpath).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.page_login_button_xpath).click()

def wait_for_load(driver, waiting_element):
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, waiting_element)))

def wait_for_load_burger_ingredients(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, Locators.burger_ingredients)))


""" Успешная регистрация """
def test_registration_success(driver):
    driver.get(Urls.page_register_url)
    driver.find_element(By.XPATH, Locators.name_auth).send_keys(random_name)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(f'{random_name}@mail.ru')
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys(f'{random.randint(100000, 9999999)}')
    driver.find_element(By.XPATH, Locators.button_auth).click()
    wait_for_load(driver, Locators.entrance_login_page)
    assert driver.current_url == Urls.page_login_url


""" Регистрация - ошибка для некорректного пароля """
def test_registration_incorrect_password(driver):
    driver.get(Urls.page_register_url)
    set_auth_name_and_email(driver)
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys('12345')
    driver.find_element(By.XPATH, Locators.button_auth).click()
    wait_for_load(driver, Locators.incorrect_password_text)
    assert driver.find_element(By.XPATH, Locators.incorrect_password_text).text == "Некорректный пароль"


""" Регистрация существующего пользователя  """
def test_registration_existing_user(driver):
    driver.get(Urls.page_register_url)
    set_auth_name_and_email(driver)
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys(Locators.user_password)
    driver.find_element(By.XPATH, Locators.button_auth).click()
    wait_for_load(driver, Locators.text_user_is_exists)
    assert driver.find_element(By.XPATH, Locators.text_user_is_exists).text == "Такой пользователь уже существует"


""" Регистрация с пустым полем "Имя" """
def test_registration_no_name(driver):
    driver.get(Urls.page_register_url)
    driver.find_element(By.XPATH, Locators.email_auth).send_keys(f'{random_name}@mail.ru')
    driver.find_element(By.XPATH, Locators.pass_auth).send_keys(f'{random.randint(100000, 9999999)}')
    driver.find_element(By.XPATH, Locators.button_auth).click()
    WebDriverWait(driver, 50)
    assert driver.current_url == Urls.page_register_url


""" Вход по кнопке «Войти в аккаунт» на главной странице """
def test_login_in_main_page(driver):
    driver.get(Urls.main_page_url)
    driver.find_element(By.XPATH, Locators.button_login_to_account_main).click()
    wait_for_load(driver, Locators.entrance_login_page)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    assert driver.current_url == Urls.main_page_url


""" Вход через кнопку "Личный кабинет"  """
def test_login_in_personal_account(driver):
    driver.get(Urls.main_page_url)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    wait_for_load(driver, Locators.entrance_login_page)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    assert driver.current_url == Urls.main_page_url


""" Вход через кнопку в форме регистрации  """
def test_login_in_registration_form(driver):
    driver.get(Urls.page_register_url)
    driver.find_element(By.XPATH, Locators.button_log_in_reg_form).click()
    wait_for_load(driver, Locators.entrance_login_page)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    assert driver.find_element(By.XPATH, Locators.fluorescent_bun).is_displayed()


""" Вход через кнопку в форме восстановления пароля  """
def test_login_in_restore_password(driver):
    driver.get(Urls.main_page_url)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    wait_for_load(driver, Locators.entrance_login_page)
    driver.find_element(By.XPATH, Locators.button_restore_password).click()
    wait_for_load(driver, Locators.restore_password)
    driver.find_element(By.XPATH, Locators.button_log_in_restore_password).click()
    wait_for_load(driver, Locators.entrance_login_page)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    assert driver.current_url == Urls.main_page_url


""" Переход из личного кабинета в конструктор  """
def test_go_to_constructor_from_personal_account(driver):
    driver.get(Urls.page_login_url)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    wait_for_load(driver, Locators.profile_title)
    driver.find_element(By.XPATH, Locators.constructor_title).click()
    wait_for_load(driver, Locators.build_burger)
    assert driver.current_url == Urls.main_page_url


""" Переход из личного кабинета на логотип Stellar Burgers """
def test_go_to_logo_from_personal_account(driver):
    driver.get(Urls.page_login_url)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    wait_for_load(driver, Locators.profile_title)
    driver.find_element(By.XPATH, Locators.logotype).click()
    wait_for_load(driver, Locators.build_burger)
    assert driver.current_url == Urls.main_page_url


""" Выход из аккаунта по кнопке "Выйти" в личном кабинете  """
def test_exit_in_personal_account(driver):
    driver.get(Urls.main_page_url)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    wait_for_load(driver, Locators.entrance_login_page)
    set_log_in(driver)
    wait_for_load(driver, Locators.build_burger)
    driver.find_element(By.XPATH, Locators.button_personal_account).click()
    wait_for_load(driver, Locators.profile_title)
    driver.find_element(By.XPATH, Locators.button_exit_personal_account).click()
    wait_for_load(driver, Locators.entrance_login_page)
    assert driver.current_url == Urls.page_login_url


"""  Переход по разделам (Начинки) """
def test_switch_to_section_fillings(driver):
    driver.get(Urls.main_page_url)
    wait_for_load_burger_ingredients(driver)
    driver.find_element(By.XPATH,Locators.fillings).click()
    assert 'tab_tab_type_current' in driver.find_element(By.XPATH,Locators.fillings_active).get_attribute("class")


"""  Переход по разделам (Соусы) """
def test_switch_to_section_sauces(driver):
    driver.get(Urls.main_page_url)
    wait_for_load_burger_ingredients(driver)
    driver.find_element(By.XPATH,Locators.sauces).click()
    assert 'tab_tab_type_current' in driver.find_element(By.XPATH,Locators.sauces_active).get_attribute("class")


"""  Переход по разделам (Булки) """
def test_switch_to_section_buns(driver):
    driver.get(Urls.main_page_url)
    wait_for_load_burger_ingredients(driver)
    driver.find_element(By.XPATH, Locators.fillings).click()
    WebDriverWait(driver, 30)
    driver.find_element(By.XPATH,Locators.buns).click()
    assert 'tab_tab_type_current' in driver.find_element(By.XPATH,Locators.buns_active).get_attribute("class")
