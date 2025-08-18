import allure
import pytest
from pages.main_page import MainPage

@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку 'тайна лисьей норы'.")
    def test_by_name(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("тайна лисьей норы")
        assert "Показываем результаты по запросу «тайна лисьей норы», найдено:" in main_page.get_search_results_text()


    @allure.title("Поиск книги с символами вместо названия")
    @allure.description("Тест проверяет поиск книги с использование символов вместо названия")
    def test_negative_by_symbols(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.search_book("%&*#")
        assert "Поиск по запросу «%&*#» не принёс результатов" in main_page.get_search_results_text()


        @allure.title("Поиск книги  с символами и нозванием ")
        @allure.description("Тест проверяет поиск книги с символами и нозванием")
        def test_negative_by_symbols(self, driver):
            main_page = MainPage(driver)
            main_page.open()
            main_page.search_book("$$$тайна лисьей норы")
            assert "показывает результаты по запросу  «$$$тайна лисьей норы» , найдено" in main_page.get_search_results_text()

            @allure.title("Поиск книги с неполным названием ")
            @allure.description("Тест проверяет поиск книги с неполным нозванием")
            def test_negative_by_symbols(self, driver):
                main_page = MainPage(driver)
                main_page.open()
                main_page.search_book(" нора")
                assert "Поиск по запросу « нора» не принёс результатов" in main_page.get_search_results_text()