import arcade

from weapons import Effect
class Consommables:
    def __init__(self, name, heal = 0, effect_to_debuff = None, stat_boost = ""):
        super().__init__()
        self.name = name
        self.heal = heal
        self.effect_to_debuff = effect_to_debuff
        self.stat_boost = stat_boost

    def use_item(self, player):
        print(f"\nVous venez d'utiliser {self.name}")

        if self.heal:
            player.hp += self.heal
            print("Vous vous êtes heal de:", self.heal, "\n")
            print("Vous avez maintenant:", player.hp)
        if self.effect_to_debuff:
            if player.status == self.effect_to_debuff.name:
                player.status = None
                print("Vous vous soignez du status de:", self.effect_to_debuff.name, "\n")
        if self.stat_boost == "defense":
            player.defense += 5
            print("Vous augmentez votre defense de:", 5, "\n")
        elif self.stat_boost == "ad":
            player.ad += 5
            print("Vous augmentez votre attaque de:", 5, "\n")

            
    
#rajouter les nom des rooms dans lesquels sont les conso
consommables_data = {
    'SAS-22-1': {
        'Spray anti-BRU': Consommables('Spray anti-BRU (-BRU)', 0, Effect('BRU')),
        'Antidote': Consommables('Antidote (-PSN)', 0, Effect('PSN')),
        'Bandage': Consommables('Bandage (-SAI)', 0, Effect('SAI')),
        'Morphine' : Consommables('Morphine (-DEF)', 0, None, "defense"),
        'Kit de secours': Consommables('Kit de secours (+HP)', 5)
    },
    'SAS-24-1': {
        'Orangina' : Consommables('Orangina (+AD)', 0, None, "ad"),
        'Kit de secours 2' : Consommables('Kit de secours 2 (+HP)', 10),
        'Bandage 2' : Consommables('Bandage 2 (-SAI)', 0, Effect('SAI')),
        'Antidote': Consommables('Antidote (-PSN)', 0, Effect('PSN')),
        'Spray anti-BRU': Consommables('Spray anti-BRU (-BRU)', 0, Effect('BRU')),
        'Morphine' : Consommables('Morphine (-DEF)', 0, None, "defense"),
    },
    'SAS-06-1': {
        'Pomme dorée': Consommables('Pomme dorée', 10, Effect('PSN'), "defense"),
        'Kit de secours 3' : Consommables('Kit de secours 3 (+HP)', 20),
        'Dose éléctrique': Consommables('Dose éléctrique (+AD)', 0, None, "ad")
    },
}