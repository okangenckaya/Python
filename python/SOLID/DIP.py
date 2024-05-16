"""
D - Dependency Inversion Principle
High-level modules should not depend on low-level modules. In addition to this, they both must depend on abstractions.
For this example, BasicCalculator is a class that is high-level and where we perform all crucial events. On the other
hand, LogKeeper is a class that is low-level and where we perform only needed events.

"""

from abc import ABC, abstractmethod


class LogKeeper(ABC):
    @abstractmethod
    def log(self, result) -> dict:
        pass


class LogProvider(LogKeeper):
    def log(self, result) -> dict:
        return {"Result": result}


class BasicCalculator:
    def __init__(self, log_keeper: LogKeeper):
        self.log_keeper = log_keeper

    def calculating(self, x, y) -> dict:
        result = x * y
        return self.log_keeper.log(result)


log_provider = LogProvider()
calculator = BasicCalculator(log_provider)
result = calculator.calculating(10, 20)
print(result)

