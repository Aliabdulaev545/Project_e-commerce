# E-commerce Core

Ядро интернет-магазина на Python: классы `Product` и `Category` с автоматическим подсчётом категорий и товаров, а также загрузка данных из JSON.

## Функционал

- **Класс `Product`** — товар с полями:
  - `name` (str) — название
  - `description` (str) — описание
  - `price` (float) — цена (может быть с копейками)
  - `quantity` (int) — количество в наличии
- **Класс `Category`** — категория товаров с полями:
  - `name` (str) — название
  - `description` (str) — описание
  - `products` (list[Product]) — список объектов `Product`
- **Атрибуты класса `Category`** (общие для всех объектов, заполняются автоматически при создании новой категории):
  - `category_count` — общее количество созданных категорий
  - `product_count` — общее количество товаров во всех категориях
- **Функция `load_data_from_json(path)`** — читает JSON-файл и создаёт объекты `Category` и `Product` (дополнительное задание).

## Структура проекта
.
├── src/
│ └── main.py # классы Product, Category и загрузка из JSON
├── tests/
│ ├── conftest.py # настройка sys.path для pytest
│ └── test_main.py # тесты
├── products.json # пример данных для загрузки
├── pyproject.toml # зависимости и настройки Poetry
├── .flake8 # конфигурация flake8
└── README.md


## Установка

```bash
poetry install

## Запуск
python src/main.py

## Тесты
pytest -v --cov=src --cov-report=term-missing --cov-report=html


## Линтеры и форматирование
black src/ tests/ --line-length=119
isort src/ tests/
flake8 src/ tests/ --max-line-length=119
mypy src/


## Лицензия
MIT (см. файл LICENSE)