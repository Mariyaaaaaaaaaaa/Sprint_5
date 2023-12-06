class Locators:

    """ Поля Имя, Email, Пароль, Кнопка "Зарегистрироваться" на странице регистрации """

    name_auth = './/fieldset[1]/div[1]/div[1]/input[1]'   #  *[@id="root"]/div[1]/main[1]/div[1]/form[1]/
    email_auth = './/fieldset[2]/div[1]/div[1]/input[1]'   #  *[@id="root"]/div[1]/main[1]/div[1]/form[1]/
    pass_auth = './/fieldset[3]/div[1]/div[1]/input[1]'   #  *[@id="root"]/div[1]/main[1]/div[1]/form[1]/
    button_auth = './/button[text()="Зарегистрироваться"]'   #  *[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]
    incorrect_password_text = './/fieldset[3]/div[1]/p[1]'   #  '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]'
    text_user_is_exists = '//*[@id="root"]/div/main/div/p[1]'
    page_register_url = 'https://stellarburgers.nomoreparties.site/register'

    #  main page:
    page_main_url = 'https://stellarburgers.nomoreparties.site/'
    button_login_to_account_main = '//*[@id="root"]/div[1]/main[1]/section[2]/div[1]/button[1]'  # Кнопка  «Войти в аккаунт» на главной странице
    button_personal_account = '//*[@id="root"]/div[1]/header[1]/nav[1]/a[1]'  #  Кнопка Личный кабинет

    # registration form
    button_sign_in = '//*[@id="root"]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]'  #  Кнопка Зарегистрироваться
    button_log_in_reg_form = '//*[@id="root"]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]'  #  Кнопка Войти в форме Регистрации
    button_restore_password = '//*[@id="root"]/div[1]/main[1]/div[1]/div[1]/p[2]/a[1]'  #  Кнопка Восстановить пароль
    button_log_in_restore_password = '//*[@id="root"]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]'  # Кнопка Войти в форме восстановления пароля

    # personal account
    button_exit_personal_account = '//*[@id="root"]/div[1]/main[1]/div[1]/nav[1]/ul[1]/li[3]/button[1]'  # кнопка "Выход" в личном кабинете
    page_login_url = 'https://stellarburgers.nomoreparties.site/login'

    """ Поля Имя, Пароль, Кнопка "Войти" на странице входа """

    name_lc = '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]'
    pass_lc = '//*[@id="root"]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]'
    button_log_in = './/*[@id="root"]/div[1]/main[1]/div[1]/form[1]/button[1]'


    button_lc = '//*[@id="root"]/div[1]/header[1]/nav[1]/a[1]/p[1]'  # кнопка «Личный кабинет»


    #  section bellow with variables for login page:
    field_email_xp = './/input[@class="text input__textfield text_type_main-default" and @type="text")]'
    field_pass_xp = './/input[@class="text input__textfield text_type_main-default" and @type="password")]'






    #