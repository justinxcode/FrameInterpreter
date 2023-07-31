import numpy as np

class ActionBuilder:
    def __init__(self):
        self.actions = {
            'ups': ['UP', 'UP_FADE', 'UP_LEFT', 'UP_LEFT_FADE', 'UP_RIGHT', 'UP_RIGHT_FADE'],
            'lefts': ['LEFT', 'LEFT_FADE', 'UP_LEFT', 'UP_LEFT_FADE', 'DOWN_LEFT', 'DOWN_LEFT_FADE'],
            'downs': ['DOWN', 'DOWN_FADE', 'DOWN_RIGHT', 'DOWN_RIGHT_FADE', 'DOWN_LEFT', 'DOWN_LEFT_FADE'],
            'rights': ['RIGHT', 'RIGHT_FADE', 'UP_RIGHT', 'UP_RIGHT_FADE', 'DOWN_RIGHT', 'DOWN_RIGHT_FADE'],
            'punchs': ['PUNCH', 'PUNCH_FADE'],
            'kicks': ['KICK', 'KICK_FADE'],
            'slashs': ['SLASH', 'SLASH_FADE'],
            'heavy_slashs': ['HEAVY_SLASH', 'HEAVY_SLASH_FADE'],
            'dusts': ['DUST', 'DUST_FADE'],
            'taunts': ['TAUNT', 'TAUNT_FADE'],
            'dashs': ['DASH', 'DASH_FADE'],
            'roman_cancels': ['ROMAN_CANCEL', 'ROMAN_CANCEL_FADE'],
            'faultless_defenses': ['FAULTLESS_DEFENSE', 'FAULTLESS_DEFENSE_FADE'],
        }

    def create_action_array(self, inputs):
        return np.array([1 if any(input in self.actions[action] for input in inputs) else 0 for action in self.actions])
