import random
    
class Combat:
    
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def est_termine(self):
        return self.pokemon1.vie <= 0 or self.pokemon2.vie <= 0
    
    def vainqueur(self):
        if self.pokemon1.vie <= 0:
            return self.pokemon2.nom
        elif self.pokemon2.vie <= 0:
            return self.pokemon1.nom
        else:
            return None
    
    def attaque_reussie(self):
        return random.randint(0, 1) == 1
    
    def puissance_attaque(self, type_adversaire):
        tableau_puissance = {
            "eau": {"feu": 2, "plante": 0.5, "eau": 0.5},
            "feu": {"plante": 2, "eau": 0.5, "feu": 0.5},
            "plante": {"eau": 2, "feu": 0.5, "plante": 0.5}
        }
        puissance = self.pokemon1.puissance_attaque
        if type_adversaire in tableau_puissance:
            puissance *= tableau_puissance[type_adversaire][self.pokemon1.type]
        return puissance
    
    def tour(self):
        if self.est_termine():
            return 
        if self.attaque_reussie():
            puissance = self.puissance_attaque(self.pokemon2.type)
            self.pokemon2.vie -= puissance
            print(f"{self.pokemon1.nom} attaque {self.pokemon2.nom} avec {self.pokemon1.attaque} et inflige {puissance} dégâts.")
        else:
            print(f"{self.pokemon1.nom} rate son attaque.")
        if not self.est_termine() and self.attaque_reussie():
            puissance = self.puissance_attaque(self.pokemon1.type)
            self.pokemon1.vie -= puissance
            print(f"{self.pokemon2.nom} attaque {self.pokemon1.nom} avec {self.pokemon2.attaque} et inflige {puissance} dégâts.")
        elif not self.est_termine():
            print(f"{self.pokemon2.nom} rate son attaque.")
