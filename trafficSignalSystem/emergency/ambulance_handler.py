from emergency.emergency_handler import EmergencyHandler

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