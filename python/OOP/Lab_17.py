# Dünyanın farklı lokasyonlarından kahve çekirdeği ithal edeceğiz.
# Lakin kahve çekirdeğinin lezzeti ve kalitesi açısından hasat zamanlarına göre bu işlemi yapacağız.
# 4 ile 7. aylar arasında Colombia'dan,
# 8 ile 11. aylar Sumatra,
# 1 ya da 2 ya da 12. aylarda African,
# 3. ayda hasat zamanı olmadığı için hiçbir yerden

from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def ship_from(self) -> str:
        pass


class ColombiaService(BaseService):
    def ship_from(self) -> str:
        return 'from Colombia'


class SumatraService(BaseService):
    def ship_from(self) -> str:
        return 'from Sumatra Island'


class AfricanService(BaseService):
    def ship_from(self) -> str:
        return 'from South Africa'


class DefaultService(BaseService):
    def ship_from(self) -> str:
        return 'not available...! '


class Shipment:
    @staticmethod
    def shipment_method(month) -> BaseService:
        if 4 <= month <= 7:
            return ColombiaService()
        elif 8 <= month <= 11:
            return SumatraService()
        else:
            if month == 1 or month == 2 or month == 12:
                return AfricanService()
            else:
                return DefaultService()


def main():
    for month in range(1, 13):
        product_shipment = Shipment.shipment_method(month)
        print(f'{month}.month: Coffe beans shipment: {product_shipment.ship_from()}')


main()