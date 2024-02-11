if __name__ == "__main__":
    """This is a main function"""
    class Product:
        """Product model"""
        def __init__(self, name: str, price: float, quality: str, sale=0):
            self.name = name
            if price <= 0 and isinstance(price, (float, int)):
                raise ValueError("Product must cost something!")
            self.price = price
            self.quality = quality
            if sale < 0 or sale > 100 and isinstance(price, (float, int)):
                raise ValueError("Enter sale in percents from 0 to 100%!")
            self.sale = sale

        def __str__(self):
            return f"{self.name}'s price is {self.price} with {self.quality}. " \
                   f"sale = {self.sale}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, price={self.price} " \
                   f"quality={self.quality}, sale={self.sale})"

        def calculate_discount(self) -> float:
            """Calc discount price"""
            return self.price * (100 - self.sale) / 100


    class Food(Product):
        """Food model"""
        def __init__(self, name: str, price: float, quality: str,
                     weight: float, calories: float, sale=0):
            super().__init__(name, price, quality, sale)
            self.weight = weight
            self.calories = calories

        def __str__(self):
            return f"{self.name}'s weight is {self.weight}. Calories: {self.calories} " \
                   f"Price is {self.price} with {self.quality} quality. " \
                   f"sale = {self.sale}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, price={self.price} " \
                   f"quality={self.quality}, sale={self.sale} " \
                   f"weight={self.weight}, calories={self.calories})"


    class Cloth(Product):
        """Cloth model"""
        def __init__(self, name: str, price: float, quality: str,
                     gear: str, color: str, sale=0):
            super().__init__(name, price, quality, sale)
            self.gear = gear
            self.color = color

        def __str__(self):
            return f"{self.name} {self.color} {self.gear} costs {self.price} (sale={self.sale}). " \
                   f"Quality is {self.quality}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, price={self.price} " \
                   f"quality={self.quality}, sale={self.sale} " \
                   f"gear={self.gear}, color={self.color})"
