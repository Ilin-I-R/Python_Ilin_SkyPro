# Проект автоматизации тестирования с Allure

Проект содержит автоматизированные тесты для веб‑приложений с использованием Selenium и Allure для отчётности.

## Структура проекта

* `base_page.py` — базовый класс для всех страниц
* `login_page.py`, `inventory_page.py`, `cart_page.py`, `checkout_page.py` — классы страниц приложения saucedemo.com
* `page_objects.py` — класс для работы с калькулятором
* `test_calculator_edge.py` — тест калькулятора
* `test_saucedemo.py` — тест полного сценария покупки на saucedemo.com

## Установка зависимостей

```bash
pip install allure-pytest pytest selenium
