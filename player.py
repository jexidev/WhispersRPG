from stat_feedback import increase_stat_feedback, decrease_stat_feedback
from engine.scene_engine import narrate

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {        
            "identity_stability":2,
            "insight":0,
            "willpower":0,
            "empathy":0,
            "curiosity":0,
            "corruption":0 
            }
        self.flags = {
            "discarded_ticket": False,}
        self.inventory = []
        self.journal = []

    def update_stat(self, stat_name, amount):
        if stat_name in self.stats:
            self.stats[stat_name] += amount
            if self.stats[stat_name] < 0:
                self.stats[stat_name] = 0

            if amount > 0:
                feedback = increase_stat_feedback.get(stat_name)
            elif amount < 0:
                feedback = decrease_stat_feedback.get(stat_name)
            else:
                feedback = None

            if feedback:
                narrate(feedback)