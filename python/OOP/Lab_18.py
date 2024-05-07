#Basic abstraction example

from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def logging_system(self) -> str:
        pass


class SystemCreator(ABC):
    def creator_function(self) -> Log:
        pass


#abstract method on more actions menu has been implemented here:
class Admin_Log(Log):
    def logging_system(self) -> str:
        return 'Welcome admin...!'


class Manager_Log(Log):
    def logging_system(self) -> str:
        return 'Welcome manager...!'


class Admin_Log_Creator(SystemCreator):
    def creator_function(self) -> Log:
        return Admin_Log()


class Manager_Log_creator(SystemCreator):
    def creator_function(self) -> Log:
        return Manager_Log()


def main():
    print('=============================')
    print('System has been opened...! ')
    print(Admin_Log_Creator().creator_function().logging_system())
    print('=============================')
    print('System has been opened...! ')
    print(Manager_Log_creator().creator_function().logging_system())
    print('=============================')


main()