
from abc import ABC, abstractmethod


class Base_instrument:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Guitar(Base_instrument):
    def __init__(self, brand, model, guitar_string):
        super().__init__(brand, model)
        self.guitar_string = guitar_string


class Violin(Base_instrument):
    def __init__(self, brand, model, violin_string):
        super().__init__(brand, model)
        self.violin_string = violin_string


class Musician:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.instruman_number = []

# Because BaseService class receives inheritence from ABC class, it is now an abstract class.
# BaseService is a class that includes functions helping for us to manage CRUD operations per entity.

class BaseService(ABC):
    @abstractmethod
    def call_sound(self) -> str:
        pass

    def hello_everyone(self) -> None:
        print('Hello everyone...!')


class GuitarService(BaseService):
    def call_sound(self) -> str:
        return 'Guitar sound...!'

    def hello_everyone(self) -> None:
        print('Salve..!')


class ViolinService(BaseService):

    def call_sound(self) -> str:
        return 'Violin sound...!'

    @staticmethod
    def harmonize():
        print('it has been tuned...!')


def main():

    guitar_service = GuitarService()
    violin_service = ViolinService()

    guitar = Guitar('yamaha', 'electric guitar', 'Well String')
    violin = Violin('Stromberg', 'Classic Violin', 'Well String')

    musician = Musician('Okan', 'Genckaya')
    musician.instruman_number.append(guitar)
    musician.instruman_number.append(violin)

    print(f'First Name: {musician.first_name}\n'
          f'Last Name: {musician.last_name}\n'
          f'Instrument Name: {musician.instruman_number[0].brand}\n'
          f'Instrument Model: {musician.instruman_number[0].model}\n'
          f'Instrument Sound: {guitar_service.call_sound()}')
    print('=============================================================')
    print(f'First Name: {musician.first_name}\n'
          f'Last Name: {musician.last_name}\n'
          f'Instrument Name: {musician.instruman_number[1].brand}\n'
          f'Instrument Model: {musician.instruman_number[1].model}\n'
          f'Instrument Sound: {violin_service.call_sound()}')

    violin_service.harmonize()


main()

