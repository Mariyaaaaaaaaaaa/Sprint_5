class Locators:

    """  Urls  """

    main_page_url = 'https://stellarburgers.nomoreparties.site/'
    page_register_url = 'https://stellarburgers.nomoreparties.site/register'
    page_login_url = 'https://stellarburgers.nomoreparties.site/login'


    """  User_credentials  """

    user_name = 'Maria'
    user_email = 'shcherbakova_sun999@yandex.ru'
    user_password = '2421484'


    """  Поля на странице регистрации  """

    name_auth = './/fieldset[1]/div/div/input'  # Поле "Имя"
    email_auth = './/fieldset[2]/div/div/input'  # Поле "Email"
    pass_auth = './/fieldset[3]/div/div/input'   # Поле " Пароль"
    button_auth = './/button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    incorrect_password_text = './/p[text()="Некорректный пароль"]'  # текст "Некорректный пароль"
    text_user_is_exists = './/p[text()="Такой пользователь уже существует"]'  # текст "Такой пользователь уже существует"
    button_log_in_reg_form = './/a[@class="Auth_link__1fOlj" and text()="Войти"]'  # Кнопка "Войти" в форме регистрации


    """  Поля Имя, Пароль, Кнопка "Войти" на странице входа в Личном кабинете  """

    field_email_xpath = ".//input[(@class='text input__textfield text_type_main-default' and @type='text')]"
    field_password_xpath = ".//input[(@class='text input__textfield text_type_main-default' and @type='password')]"
    page_login_button_xpath = ".//button[(@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')]"


    """  Main page """

    button_login_to_account_main = './/button[text()="Войти в аккаунт"]'  # Кнопка  «Войти в аккаунт» на главной странице
    button_personal_account = './/p[text()="Личный Кабинет"]'  # Кнопка "Личный Кабинет" на главной странице


    """ Personal account  """

    button_restore_password = './/a[text()="Восстановить пароль"]'  # Кнопка "Восстановить пароль"
    button_log_in_restore_password = './/a[@class="Auth_link__1fOlj" and text()="Войти"]'  # Кнопка "Войти" в форме восстановления пароля
    button_exit_personal_account = './/button[text()="Выход"]'  # Кнопка "Выход" в личном кабинете
