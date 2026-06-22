from abc import ABC, abstractmethod

class EmergencyHandler(ABC):

    @abstractmethod
    def handle_emergency(
        self,
        direction
    ):
        pass