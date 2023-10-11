from selenium.webdriver.common.by import By


class CompanyRating():
    PRESS_TO_RATING = (By.XPATH, "//a[text()='Рейтинг']")
    LINK_TO_COMPANY_RATING = (By.XPATH, "//*[@class='companies_ratings_page']")
    CLICK_TO_LIST_PERIOD_FOR_COMPANY_RATING = (By.XPATH, "//*[@class='ratings-page-header__period-switch']")
    SELECT_2021_YEAR_FOR_COMPANY_RATING = (By.XPATH, "//*[@value='2021']")

class ApiServices():
    PRESS_TO_API_SERVICES = (By.XPATH, "//a[@href='https://career.habr.com/info/api']")

class Vacancies():
    CLICK_TO_VACANCIES = (By.XPATH, "//a[@href='https://career.habr.com/vacancies']")
    CLICK_TO_CHOICE_A_SPEZIALIZATION = (By.XPATH, "//*[contains(text(), 'Выберите специализацию')]")
    CLICK_TO_TESTING_IN_SPEZIALIZATION = (By.XPATH, "//*[contains(text(), ' Тестирование ')]")
    SELECT_TO_AUTOMATION_ENGINEER = (By.XPATH, "//*[contains(text(), ' Инженер по автоматизации тестирования ')]")
    CLICK_TO_BUTTON_APPLY_IN_SPEZIALIZATION = (By.XPATH, "//*[contains(text(), ' Применить ')]")
    CLICK_TO_SEARCH_IN_VACANCIES = (By.XPATH, "//input[@placeholder='Поиск']")
    SELECT_A_VACANCY_ACCORDING_TO_SORTING = (By.XPATH, "//a[@href='/vacancies/1000132108']")  # Здесь выбрали рандомную вакансию
    # которая соответствовала нашей сортировке
    SELECT_A_TESTER_VACANCY = (By.XPATH, "//a[@href='/vacancies/1000130883']")   # Здесь выбрали рандомную вакансию
    # которая соответствовала нашему условию

class Habr_Communities_Of_IT_Specialists():
    CLICK_TO_ALL_HABR_SERVICES = (By.XPATH, "//*[@class='tm-panel__projects-dropdown mq-not-mobile']")
    SELECT_HABR_COMMUNITIES_OF_IT_SPECIALISTS = (By.XPATH, "//*[contains(text(), 'Сообщество IT-специалистов')]")

class Articles_In_The_Community_Of_IT_Specialists():
    SELECT_AN_ARTICLE_BY_SORT_IN_HABR = (By.XPATH, "//a[@href='/ru/articles/766854/']")
    # Здесь выбрали рандомную статью которая соответствовала нашей сортировке

class Substring_To_Search_For_Specialists_On_The_Main_Page():
    CLICK_TO_SUBSTRING_TO_SEARCH_FOR_SPECIALISTS_ON_THE_MAIN_PAGE = (By.XPATH, "//input[@name='q']")
    CLICK_ON_THE_FIND_BUTTON_FOR_SPECIALISTS_ON_THE_MAIN_PAGE = (By.XPATH, "//*[contains(text(), 'Найти')]")















