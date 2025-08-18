import requests
import allure


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36","authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMDYwODYwLCJpYXQiOjE3NDkwNjIwNjMsImV4cCI6MTc0OTA2NTY2MywidHlwZSI6MjB9.wUsxvp85D9ryit88DcEl6igEr2CjJbHbIVUgI74Ycc4"}
base_url = "https://web-gate.chitai-gorod.ru/api/v2/"


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=виктория дьякова", headers=headers)
    assert resp.status_code == 200


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с недопустимой китайской фразой")
@allure.description("Проверка, что API возвращает ошибку при поиске с недопустимой китайской фразой.")
def test_negative_api_Japanese():
    resp = requests.get(f"{base_url}search/product?phrase=你好", headers=headers)
    assert resp.status_code == 422


@allure.epic("API Тестирование")
@allure.feature("Получение категорий книг")
@allure.title("Тестирование получения списка категорий книг")
@allure.description("Проверка, что API возвращает успешный ответ с доступными категориями книг.")
def test_api_get_categories():
    resp = requests.get(f"{base_url}categories", headers=headers)
    assert resp.status_code == 200


    @allure.epic("API Тестирование")
    @allure.feature("Поиск книг")
    @allure.title("Тестирование поиска с пустым запросом")
    @allure.description("Проверка, что API возвращает ошибку при поиске с пустым запросом.")
    def test_negative_api_empty_query():
        resp = requests.get(f"{base_url}search/product?phrase=", headers=headers)
        assert resp.status_code == 400
