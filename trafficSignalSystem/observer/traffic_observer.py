from abc import ABC, abstractmethod

class TrafficObserver(ABC):

    @abstractmethod
    def update(
        self,
        intersection_id,
        direction,
        color
    ):
        pass