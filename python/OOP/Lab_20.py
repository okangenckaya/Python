from abc import ABC, abstractmethod
from datetime import datetime


class BaseEntity:
    def __init__(self, bill_name, amount, value_add_tax,):
        self.value_add_tax = value_add_tax
        self.amount = amount
        self.bill_name = bill_name


class WaterBill(BaseEntity):
    def __init__(self,bill_name, amount, value_add_tax, mill):
        super().__init__(bill_name, amount, value_add_tax)
        self.mill = mill


class ElectricityBill(BaseEntity):
    def __init__(self, bill_name, amount, value_add_tax, kw):
        super().__init__(bill_name, amount, value_add_tax)
        self.kw = kw


class NaturalGasBill(BaseEntity):
    def __init__(self, bill_name, amount, value_add_tax, m3):
        super().__init__(bill_name, amount, value_add_tax)
        self.m3 = m3



class BillService(ABC):
    @abstractmethod
    def create_bill(self, bill: BaseEntity): pass


class WaterBillService(BillService):
    def create_bill(self, bill: WaterBill):
        return bill.amount * bill.value_add_tax * bill.mill


class ElectricityBillService(BillService):
    def create_bill(self, bill: ElectricityBill):
        return bill.amount * bill.value_add_tax * bill.kw


class GasBillService(BillService):
    def create_bill(self, bill: NaturalGasBill):
        return bill.amount * bill.value_add_tax * bill.m3


class Utilities:
    @staticmethod
    def log_creator(bill_name: str, total_amount: float) -> None:
        with open(file='bill_data_collector.txt', mode='a', encoding='UTF-8') as file:
            file.write(f'Bill Name: {bill_name}\n'
                       f'Create Date: {datetime.now()}\n'
                       f'Total Amount: {total_amount}')


def main():

    water_services = WaterBillService()
    electricity_services = ElectricityBillService()
    natural_gas_services = GasBillService()

    water_bill = WaterBill('water', 100, 18.5, 100)
    total_amount = water_services.create_bill(water_bill)
    print(f'The amount you have to pay: {total_amount}')
    Utilities.log_creator(water_bill.bill_name, total_amount)


main()
