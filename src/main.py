import json
from typing import List


class Product:
    """Класс для описания товара в интернет-магазине."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для описания категории товаров."""

    name: str
    description: str
    products: List[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса при создании нового объекта
        Category.category_count += 1
        Category.product_count += len(products)


def load_data_from_json(file_path: str) -> List[Category]:
    """Загружает категории и товары из JSON-файла и возвращает список объектов Category."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories: List[Category] = []
    for category_data in data:
        products = [
            Product(
                name=p["name"],
                description=p["description"],
                price=p["price"],
                quantity=p["quantity"],
            )
            for p in category_data.get("products", [])
        ]
        categories.append(
            Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
        )
    return categories


if __name__ == "__main__":
    # Демонстрация работы (можно удалить/заменить на реальный код)
    product1 = Product("Ноутбук", "Игровой ноутбук", 150000.50, 5)
    product2 = Product("Мышь", "Беспроводная мышь", 2500.00, 20)

    category1 = Category("Электроника", "Техника и гаджеты", [product1, product2])

    print(f"Категорий: {Category.category_count}")
    print(f"Товаров: {Category.product_count}")
    print(f"В категории '{category1.name}': {len(category1.products)} товаров")

    # Доп. задание: загрузка из JSON
    # categories = load_data_from_json("products.json")
    # print(f"Загружено категорий: {len(categories)}")
