import allure
import pytest
from pages.main_page import MainPage

@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку 'капитанская'.")
    def test_by_name(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("капитанская")
        assert "Показываем результаты по запросу «капитанская», найдено:" in main_page.get_search_results_text()


    @allure.title("Поиск книги с символами вместо названия")
    @allure.description("Тест проверяет поиск книги с использование символов вместо названия")
    def test_negative_by_symbols(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("#$%")
        assert "Поиск по запросу «#$%» не принёс результатов" in main_page.get_search_results_text()