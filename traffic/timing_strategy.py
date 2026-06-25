class timing_strategy:
    def __init__(self, phase):
        self.phase = phase

class normal_timing_strategy(timing_strategy):
    def __init__(self, phase):
        super().__init__(phase)
        
    def get_phase_duration(self):
        return self.phase.duration
    
class heavy_traffic_timing_strategy(timing_strategy):
    def __init__(self, phase):
        super().__init__(phase)
        
    def get_phase_duration(self):
        return self.phase.duration * 2