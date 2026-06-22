from strategy.timing_strategy import TimingStrategy

class NormalStrategy(
      TimingStrategy
):

    def get_green_duration(
        self,
        phase
    ):
        return phase.green_duration