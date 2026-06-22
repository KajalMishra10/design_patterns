from abc import ABC, abstractmethod

class TimingStrategy(ABC):

    @abstractmethod
    def get_green_duration(
        self,
        phase
    ):
        pass