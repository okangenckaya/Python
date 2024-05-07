# Basic Credit Card Payment Data

from abc import ABC, abstractmethod


class CreditCardElements:
    def __init__(self):
        self.bank = ''
        self.card_type = ''
        self.card_limit = 0
        self.payment_by_installment = False


class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCardElements()

    @property
    def credit_card_itself(self) -> CreditCardElements:
        return self._credit_card

    @abstractmethod
    def bank_name_function(self) -> str: pass

    @abstractmethod
    def card_type_function(self) -> str: pass

    @abstractmethod
    def card_limit(self) -> float: pass

    @abstractmethod
    def installment_system_function(self) -> bool: pass


class VisaCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card_itself

    def bank_name_function(self) -> str:
        self._credit_card.bank = 'Yapı Kredi'
        return self._credit_card.bank

    def card_type_function(self) -> str:
        self._credit_card.card_type = 'Visa'
        return self._credit_card.card_type

    def installment_system_function(self) -> bool:
        self._credit_card.payment_by_installment = True
        return self._credit_card.payment_by_installment

    def card_limit(self) -> float:
        self._credit_card.card_limit = 15000
        return self._credit_card.card_limit


class Mastercard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card = super().credit_card_itself

    def bank_name_function(self) -> str:
        self._credit_card.bank = 'Akbank'
        return self._credit_card.bank

    def card_type_function(self) -> str:
        self._credit_card.card_type = 'Mastercard'
        return self._credit_card.card_type

    def installment_system_function(self) -> bool:
        self._credit_card.payment_by_installment = True
        return self._credit_card.payment_by_installment

    def card_limit(self) -> float:
        self._credit_card.card_limit = 17000
        return self._credit_card.card_limit


class Card_Creator:

    @staticmethod
    def creating_credit_card(credit_card_builder: CreditCardBuilder):
        print(f'Bank Name: {credit_card_builder.bank_name_function()}')
        print(f'Credit Card Type: {credit_card_builder.card_type_function()}')
        print(f'Installment Payment: {credit_card_builder.installment_system_function()}')
        print(f'Card Limit: {credit_card_builder.card_limit()}')


def main():

    print("=================================")
    Card_Creator.creating_credit_card(VisaCard())
    print("=================================")
    Card_Creator.creating_credit_card(Mastercard())
    print("=================================")


main()









