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
            "quantity": 0,
        }
        if product_id not in self.cart.keys():
            self.cart[product_id] = data
            self._save()
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
            self._save()
            return None
        else:
            self.cart[product_id]["quantity"] += quantity
            print(self.cart[product_id])
        self._save()
        print("кол-во", quantity)
        print("add:", product_id)
        print(type(product_id))

        return data

    def _save(self):
        print(self.cart)
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def delete(self, product_id:int):
        """
        Удаление товара из корзины.
        """
        print(type(product_id))
        print(self.cart)
        if product_id in self.cart.keys():
            del self.cart[product_id]
            self._save()

    def decrement(self, product_id: int):
        product = self.cart.get(product_id)
        if product is not None:
            quantity = product["quantity"] - 1
            self.add(product_id, "", 0, quantity, update_quantity=True)
    def clear(self):
         # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    # def get_total_price(self):
    #     """
    #     Подсчет стоимости товаров в корзине.
    #     """
    #     return sum(
    #         Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
    #     )

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        for item in self.cart.values():
            item["price"] = int(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item
