from datetime import datetime


class BaseEntity:
    def __init__(self, bill_name, value_add_task, amount):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount
        self.create_date = datetime.now()

    def bill_calculator(self) -> float:
        return self.value_add_task * self.amount

    def create_log(self):
        with open(file='bill_data.txt', mode='a', encoding='UTF-8') as file:
            file.write(f'Bill Name: {self.bill_name}\n'
                       f'Total Amount: {self.bill_calculator()}\n'
                       f'Date: {datetime.now()}')


class WaterBill(BaseEntity):
    def __init__(self, bill_name, value_add_task, amount, mill):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill

    def bill_calculator(self) -> float:
        return self.mill * self.amount


class Electricity(BaseEntity):
    def __init__(self, bill_name, value_add_task, amount, kw):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw

    def bill_calculator(self) -> float:
        return self.kw * self.amount


class NaturalGas(BaseEntity):
    def __init__(self, bill_name, value_add_task, amount, m3):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3

    def bill_calculator(self) -> float:
        return self.m3 * self.amount

    def create_log(self):
        super().create_log()
        with open(file='bill_data.txt', mode='a', encoding='UTF-8') as file:
            file.write(f'')


water_bill = WaterBill('ISKI', 135.2, 190, 90)
water_bill.create_log()





