#Overriding

from uuid import uuid4


class BasePhone:
    def __init__(self, brand, model, price):
        self.phone_id = uuid4()
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self) -> None:
        print(f'Model: {self.model}\n'
              f'Brand: {self.brand}\n'
              f'Phone Id: {self.phone_id}')

    def phone_ring_sound(self) -> None:
        print('General Phone Sound.')


class Samsung(BasePhone):
    def __init__(self, brand, model, price, operating_system):
        super().__init__(brand, model, price)
        self.operating_system = operating_system

    def phone_ring_sound(self) -> None:
        print('Samsung Phone Sound...!')

    def show_info(self) -> None:
        super().show_info()
        print(f'Operating System: {self.operating_system}')


class Iphone(BasePhone):
    def __init__(self, brand, model, price, camera_object):
        super().__init__(brand, model, price)
        self.camera = camera_object

    def phone_ring_sound(self) -> None:
        print('Iphone Phone Sound')

    def show_info(self) -> None:
        super().show_info()
        print(f'Camera: {self.camera}')


samsung = Samsung(brand='Samsung', model='S23 Ultra', price=55019, operating_system='Android')
samsung.show_info()
samsung.phone_ring_sound()

iPhone = Iphone('iPhone', '14 Pro Max', 67118, 'Pro Camera System')
iPhone.show_info()
iPhone.phone_ring_sound()

