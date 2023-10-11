from pages.main_page import MainPage
import pytest
import allure

link = "https://career.habr.com/"

@allure.description("Check the guest can view the rating of companies for the selected period")
@pytest.mark.smoke
def test_the_guest_can_view_the_rating_of_companies_for_the_selected_period(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    browser.maximize_window()
    page.open()
    page.go_to_company_rating()
    page.select_a_specific_company_rating_period()   # В данном случае для проверки выбрали период 2021 года

@allure.description("Check go to api services")
@pytest.mark.smoke
def test_go_to_api_services(browser):
    page = MainPage(browser, link)
    browser.maximize_window()
    page.open()
    page.go_to_api_services()

@allure.description("Check the guest can go to the vacancy by applying a selection")
@pytest.mark.smoke
def test_the_guest_can_go_to_the_vacancy_by_applying_a_selection(browser):
    page = MainPage(browser, link)
    browser.maximize_window()
    page.open()
    page.go_to_vacancies()
    page.choice_of_specialization()
    page.click_to_button_apply_in_spezialization()
    page.click_to_search_in_vacancies_and_enter_python()
    page.select_any_a_vacancy_according_to_sorting()

@allure.description("Check the guest can go to an article in the community of IT specialists")
@pytest.mark.smoke
def test_the_guest_can_go_to_an_article_in_the_community_of_IT_specialists(browser):
    page = MainPage(browser, link)
    browser.maximize_window()
    page.open()
    page.go_to_habr_communities_of_it_specialists()
    page.select_any_article_in_the_community_of_IT_specialists()

@allure.description("Check the guest can find a vacancy through a search on the main page")
@pytest.mark.smoke
def test_the_guest_can_find_a_vacancy_through_a_search_on_the_main_page(browser):
    page = MainPage(browser, link)
    browser.maximize_window()
    page.open()
    page.click_to_search_for_specialists_on_the_main_page_and_enter_a_tester()
    page.click_on_the_find_button_for_specialists_on_the_main_page()
    page.select_a_tester_vacancy()










