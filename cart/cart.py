from django.conf import settings


class Cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart: dict = cart

    def add(
        self,
        product_id: int,
        name: str,
        price: int,
        quantity: int = 1,
        update_quantity: bool = False,
    ) -> dict:
        data = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity,
        }
        if product_id not in self.cart:
            self.cart[product_id] = data
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self._save()
        return data

    def _save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    # def remove(self, spacer=None, type=None, product_id=None):
    #     """
    #     Удаление товара из корзины.
    #     """
    #     if product_id:
    #         del self.cart[product_id]
    #         self.save()
    #         return
    #     product_id = str(spacer.id) + "_" + type
    #     if product_id in self.cart:
    #         del self.cart[product_id]
    #         self.save()

    # def clear(self):
    #     # удаление корзины из сессии
    #     del self.session[settings.CART_SESSION_ID]
    #     self.session.modified = True

    # def get_total_price(self):
    #     """
    #     Подсчет стоимости товаров в корзине.
    #     """
    #     return sum(
    #         Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
    #     )

    # def __len__(self):
    #     """
    #     Подсчет всех товаров в корзине.
    #     """
    #     return sum(item["quantity"] for item in self.cart.values())

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        for item in self.cart.values():
            item["price"] = int(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item
