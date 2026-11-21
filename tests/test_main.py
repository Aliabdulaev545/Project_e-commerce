import json

import pytest

from main import Category, Product, load_data_from_json


@pytest.fixture(autouse=True)
def reset_class_counters():
    """Сбрасывает атрибуты класса Category перед каждым тестом для изоляции."""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def product():
    return Product(
        name="Тестовый товар",
        description="Описание товара",
        price=1999.99,
        quantity=10,
    )


@pytest.fixture
def category(product):
    return Category(
        name="Тестовая категория",
        description="Описание категории",
        products=[product],
    )


# --- Тесты инициализации Product ---


def test_product_init(product):
    assert product.name == "Тестовый товар"
    assert product.description == "Описание товара"
    assert product.price == 1999.99
    assert product.quantity == 10


def test_product_types(product):
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)


# --- Тесты инициализации Category ---


def test_category_init(category, product):
    assert category.name == "Тестовая категория"
    assert category.description == "Описание категории"
    assert len(category.products) == 1
    assert category.products[0] is product
    assert isinstance(category.products, list)


# --- Тесты подсчёта товаров ---


def test_product_count_single_category(product):
    Category("Категория 1", "Описание", [product])
    assert Category.product_count == 1


def test_product_count_multiple_categories(product):
    product2 = Product("Товар 2", "Описание", 500.00, 3)
    Category("Категория 1", "Описание", [product])
    Category("Категория 2", "Описание", [product2, product])
    assert Category.product_count == 3


def test_product_count_empty_category():
    Category("Пустая категория", "Описание", [])
    assert Category.product_count == 0


# --- Тесты подсчёта категорий ---


def test_category_count_zero():
    assert Category.category_count == 0


def test_category_count_increments(product):
    Category("Категория 1", "Описание", [product])
    assert Category.category_count == 1

    Category("Категория 2", "Описание", [])
    assert Category.category_count == 2


def test_category_count_multiple_with_products(product):
    Category("Категория 1", "Описание", [product])
    Category("Категория 2", "Описание", [product])
    Category("Категория 3", "Описание", [])
    assert Category.category_count == 3
    assert Category.product_count == 2

    # --- Тест загрузки из JSON (доп. задание) ---

    def test_load_data_from_json(tmp_path):
        data = [
            {
                "name": "Категория",
                "description": "Описание",
                "products": [
                    {
                        "name": "Товар",
                        "description": "Описание",
                        "price": 100.0,
                        "quantity": 5,
                    }
                ],
            }
        ]
        file = tmp_path / "products.json"
        file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        categories = load_data_from_json(str(file))
        assert len(categories) == 1
        assert categories[0].name == "Категория"
        assert len(categories[0].products) == 1
        assert categories[0].products[0].price == 100.0
