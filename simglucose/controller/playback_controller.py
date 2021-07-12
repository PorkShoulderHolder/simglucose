from .base import Controller, Action


class PlaybackController(Controller):
    def __init__(self, sim_data):
        print(sim_data)
        self.history = history

    def policy(self, observation, reward, done, **kwargs):
        sample_time = kwargs.get('sample_time', 1)
        basal, bolus = self.history[sample_time]
        return Action(basal=basal, bolus=bolus)
