from observer.traffic_observer import TrafficObserver

class CentralMonitor(
      TrafficObserver
):

    def update(
        self,
        intersection_id,
        direction,
        color
    ):
        print(
            intersection_id,
            direction,
            color
        )
        