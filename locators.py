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

    field_email_xpath = './/input[@type="text" and @name="name"]'
    field_password_xpath = './/input[@type="password" and @name="Пароль"]'
    page_login_button_xpath = './/button[text()="Войти"]'


    """  Main page """

    button_login_to_account_main = './/button[text()="Войти в аккаунт"]'  # Кнопка  «Войти в аккаунт» на главной странице
    button_personal_account = './/p[text()="Личный Кабинет"]'  # Кнопка "Личный Кабинет" на главной странице
    entrance_login_page = './/h2[text()="Вход"]'
    build_burger = './/h1[text()="Соберите бургер"]'
    constructor_title = './/p[text()="Конструктор"]'
    logotype = './/div[@class="AppHeader_header__logo__2D0X2"]'
    burger_ingredients = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo'
    fluorescent_bun = './/img[@alt="Флюоресцентная булка R2-D3"]'
    fillings = './/span[text() = "Начинки"]'
    fillings_active = './/span[text() = "Начинки"]/parent::div'
    sauces = './/span[text() = "Соусы"]'
    sauces_active = './/span[text() = "Соусы"]/parent::div'
    buns = './/span[text() = "Булки"]'
    buns_active = './/span[text() = "Булки"]/parent::div'


    """ Personal account  """

    button_restore_password = './/a[text()="Восстановить пароль"]'  # Кнопка "Восстановить пароль"
    button_log_in_restore_password = './/a[@class="Auth_link__1fOlj" and text()="Войти"]'  # Кнопка "Войти" в форме восстановления пароля
    button_exit_personal_account = './/button[text()="Выход"]'  # Кнопка "Выход" в личном кабинете
    profile_title = './/a[text()="Профиль"]'


    """ Восстановление пароля  """

    restore_password = './/h2[text()="Восстановление пароля"]'
