from .base import Controller, Action
from dateutil import parser
from datetime import timedelta


class PlaybackController(Controller):
    def __init__(self, data):
        sim_data = data["sim_data"]
        self.start_time = parser.parse(data["sim_data"][0]["t"])
        self.iter = 0
        self.history = []
        for s in sim_data:
            self.history.append(s["insulin"])

    def policy(self, observation, reward, done, **kwargs):
        insulin = self.history[self.iter]
        sample_time = kwargs.get('sample_time', 1)
        self.iter += 1
        # use basal / bolus convention.  The two are collapsed in the eyes
        # of the simulator anyways so it doesnt matter.
        default_basal = 0
        bolus = insulin / sample_time
        return Action(basal=default_basal, bolus=bolus)
