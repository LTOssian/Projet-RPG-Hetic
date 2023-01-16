import arcade
from random import randint

class Effect:
    def __init__(self, name):
        self.name = name
        if self.name == 'BRU':
            self.damage_tick = 5
            self.probability = .4
        if self.name == 'PSN':
            self.damage_tick = 2
            self.probability = .2
        if self.name == 'PEU':
            self.damage_tick = 5
            self.probability = .1
        if self.name == 'SAI':
            self.damage_tick = 5
            self.probability = .1
        if self.name == 'CRT':
            self.damage_tick = 8
            self.probability = .4   
        if self.name == "LIF":
            self.damage_tick = 5
            self.probability = 1

    def get_name(self):
        return self.name

    def use_effect(self, target): 
        if randint(0, 10)/10 < self.probability:
            target.status = self.name
            return f"Additional damage dealt due to {self.name}", self.damage_tick
        else:
            return "", 0
#rajouter le nom des rooms dans lesquels sont les armes
weapon_data = {
    'SAS-10-1': {
        'Clé à molette': {'damage': 5, 'effect': None}
    },
    'SAS-22-1': {
        'Tuyau': {'damage': 5, 'effect': None},
        'Couteau de combat': {'damage': 5, 'effect': Effect("SAI")},
    },
    'SAS-06-1': {
        'Masse': {'damage': 5, 'effect': Effect("PEU")},
        'Pistolet à cloue': {'damage': 5, 'effect': Effect("PSN")},
    },
    'SAS-03': {
        'Exo Gant': {'damage': 5, 'effect': None},
    },
    'SAS-14': {
        'Blaster': {'damage': 5, 'effect': Effect('BRU')},
    },
    'SAS-05': {
        'Fusil à pompe': {'damage': 5, 'effect': None},
    },
    'SAS-23': {
        'Lance-Flamme': {'damage': 5, 'effect': Effect('BRU')},
    },
    'SAS-24-1': {
        'Taser': {'damage': 5, 'effect': Effect("PEU")}
    },
}