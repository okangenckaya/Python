
# We created BaseEntity class for objects here.
# Model page means reflector of data base on application side.
# Example below is equal to SQL logic.

from enum import Enum
from socket import gethostname, gethostbyname
from datetime import datetime


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.created_time = datetime.now()
        self.status = Status.Active.value
        self.machine_name = gethostname()
        self.ip_address = gethostbyname(gethostname())


class Category(BaseEntity):
    def __init__(self, name, description):
        super().__init__()
        self.description = description
        self.name = name

