from abc import ABC, abstractmethod

class EmergencyHandler(ABC):

    @abstractmethod
    def handle_emergency(
        self,
        direction
    ):
        pass

class AmbulanceHandler(
      EmergencyHandler
):

    def __init__(
        self,
        controller
    ):
        self.controller = controller

    def handle_emergency(
        self,
        direction
    ):
        self.controller.set_green(
            direction
        )
        