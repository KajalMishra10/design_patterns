from strategy.timing_strategy import TimingStrategy

class HeavyTrafficStrategy(
      TimingStrategy
):

    def get_green_duration(
        self,
        phase
    ):
        return phase.green_duration * 2