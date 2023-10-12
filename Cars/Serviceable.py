from abc import ABC, abstractmethod


# unsure how works
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
