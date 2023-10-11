import time
import allure

from pages.base_page import BasePage
from .locators import CompanyRating
from .locators import ApiServices
from .locators import Vacancies
from .locators import Habr_Communities_Of_IT_Specialists
from .locators import Articles_In_The_Community_Of_IT_Specialists
from .locators import Substring_To_Search_For_Specialists_On_The_Main_Page

@allure.epic("Smoke test for website habr career")
class MainPage(BasePage):
    def go_to_company_rating(self):
        press_to_company_rating = self.browser.find_element(*CompanyRating.PRESS_TO_RATING)
        press_to_company_rating.click()
        assert self.is_element_present(*CompanyRating.LINK_TO_COMPANY_RATING), "The link to the company rating is " \
                                                                                        "not presented"
    def select_a_specific_company_rating_period(self):
        click_to_list_period_for_company_rating = self.browser.find_element(*CompanyRating.CLICK_TO_LIST_PERIOD_FOR_COMPANY_RATING)
        click_to_list_period_for_company_rating.click()
        select_2021_year_for_company_rating = self.browser.find_element(*CompanyRating.SELECT_2021_YEAR_FOR_COMPANY_RATING)
        select_2021_year_for_company_rating.click()

    def go_to_api_services(self):
        click_to_api_services = self.browser.find_element(*ApiServices.PRESS_TO_API_SERVICES)
        click_to_api_services.click()

    def go_to_vacancies(self):
        click_to_vacancies = self.browser.find_element(*Vacancies.CLICK_TO_VACANCIES)
        click_to_vacancies.click()

    def choice_of_specialization(self):
        click_to_choice_a_spezialization = self.browser.find_element(*Vacancies.CLICK_TO_CHOICE_A_SPEZIALIZATION)
        click_to_choice_a_spezialization.click()
        time.sleep(1)
        click_to_testing_in_spezialization = self.browser.find_element(*Vacancies.CLICK_TO_TESTING_IN_SPEZIALIZATION)
        click_to_testing_in_spezialization.click()
        time.sleep(1)
        select_to_automation_engineer = self.browser.find_element(*Vacancies.SELECT_TO_AUTOMATION_ENGINEER)
        select_to_automation_engineer.click()
        time.sleep(1)

    def click_to_button_apply_in_spezialization(self):
        click_to_button_apply_in_spezialization = self.browser.find_element(*Vacancies.CLICK_TO_BUTTON_APPLY_IN_SPEZIALIZATION)
        click_to_button_apply_in_spezialization.click()
        time.sleep(1)

    def click_to_search_in_vacancies_and_enter_python(self):
        click_to_search_in_vacancies = self.browser.find_element(*Vacancies.CLICK_TO_SEARCH_IN_VACANCIES)
        click_to_search_in_vacancies.send_keys("Python")

    def select_any_a_vacancy_according_to_sorting(self):
        select_a_vacancy_according_to_sorting = self.browser.find_element(*Vacancies.SELECT_A_VACANCY_ACCORDING_TO_SORTING)
        select_a_vacancy_according_to_sorting.click()

    def go_to_habr_communities_of_it_specialists(self):
        click_to_all_habr_services = self.browser.find_element(*Habr_Communities_Of_IT_Specialists.CLICK_TO_ALL_HABR_SERVICES)
        click_to_all_habr_services.click()
        select_habr_communities_of_it_specialists = self.browser.find_element\
            (*Habr_Communities_Of_IT_Specialists.SELECT_HABR_COMMUNITIES_OF_IT_SPECIALISTS)
        select_habr_communities_of_it_specialists.click()

    def select_any_article_in_the_community_of_IT_specialists(self):
        select_an_article_by_sort_in_habr = self.browser.find_element\
            (*Articles_In_The_Community_Of_IT_Specialists.SELECT_AN_ARTICLE_BY_SORT_IN_HABR)
        select_an_article_by_sort_in_habr.click()

    def click_to_search_for_specialists_on_the_main_page_and_enter_a_tester(self):
        click_to_substring_to_search_for_specialists_on_the_main_page = self.browser.find_element\
            (*Substring_To_Search_For_Specialists_On_The_Main_Page.CLICK_TO_SUBSTRING_TO_SEARCH_FOR_SPECIALISTS_ON_THE_MAIN_PAGE)
        click_to_substring_to_search_for_specialists_on_the_main_page.send_keys("Тестировщик")

    def click_on_the_find_button_for_specialists_on_the_main_page(self):
        click_on_the_find_button_for_specialists_on_the_main_page = self.browser.find_element\
            (*Substring_To_Search_For_Specialists_On_The_Main_Page.CLICK_ON_THE_FIND_BUTTON_FOR_SPECIALISTS_ON_THE_MAIN_PAGE)
        click_on_the_find_button_for_specialists_on_the_main_page.click()

    def select_a_tester_vacancy(self):
        select_a_tester_vacancy = self.browser.find_element(*Vacancies.SELECT_A_TESTER_VACANCY)
        select_a_tester_vacancy.click()












