exp_table = {1:100, 2:250, 3:450, 4:650, 5:900, 6:1300, 7:1800, 8:2300, 9:2700, 10:3000}

class Pokemon:
    def __init__(self, name, level, element_type, max_hp, current_hp, current_exp, ko= False):
        self.name = name
        self.level = level
        self.type = element_type
        self.maxhp = max_hp
        self.currenthp = current_hp
        self.exp = current_exp
        self.ko_status = ko

    def __repr__(self):
        return self.name

    def lose_health(self, damage):
        self.currenthp -= damage
        if self.currenthp > 0:
            print('{} took {} damage and is now at {} HP!'.format(self.name, damage, self.currenthp))
        else:
            print('{} took {} damage and has been knocked out!'.format(self.name, damage))

    def gain_health(self, heal_amount):
        if self.ko_status == True:
            self.currenthp += heal_amount
            print('{} recovered {} health and is now at {} HP!'.format(self.name, heal_amount, self.currenthp))
            self.revive()

    def knockout(self):
        self.ko_status = True
        print('{} is at 0 HP! {} was knocked out!'.format(self.name, self.name))

    def revive(self, recovery_amount):
        self.ko_status = False
        self.currenthp = recovery_amount
        print('{} has recovered from being knocked out! {} is now at {} HP!'.format(self.name, self.name, self.currenthp))

#Will be used once a pokemon is reduced to 0 HP
    def battle_victory(self, exp_amount):
        self.exp += exp_amount
        for key in exp_table.keys():
            if self.level >= key:
                pass
            elif self.exp >= exp_table[key]:
                self.level = key
                self.exp = 0

class FireType(Pokemon):
    def __init__(self, *args, **kwargs):
        super(FireType, self).__init__(*args, **kwargs)

#determines the effectiveness of an attack against a given target
    def attack(self, target):
        if self.ko_status == True:
            print('This Pokemon has been knocked out and can no longer attack!')
        elif self.type == 'Fire' and target.type == 'Grass':
            print('{} used a super effective attack!'.format(self.name))
            target.lose_health(self.level * 2)

        elif self.type == 'Fire' and target.type == 'Water':
            print('{}\'s attack was not very effective...'.format(self.name))
            target.lose_health(self.level / 2)

        elif self.type == 'Fire' and target.type == 'Fire':
            print('{} attacks {}.'.format(self.name, target.name))
            target.lose_health(self.level)

class WaterType(Pokemon):
    def __init__(self, *args, **kwargs):
        super(WaterType, self).__init__(*args, **kwargs)

#determines the effectiveness of an attack against a given target
    def attack(self, target):
        if self.ko_status == True:
            print('This Pokemon has been knocked out and can no longer attack!')
        elif self.type == 'Water' and target.type == 'Fire':
            print('{} used a super effective attack!'.format(self.name))
            target.lose_health(self.level * 2)

        elif self.type == 'Water' and target.type == 'Grass':
            print('{}\'s attack was not very effective...'.format(self.name))
            target.lose_health(self.level / 2)

        elif self.type == 'Water' and target.type == 'Water':
            print('{} attacks {}.'.format(self.name, target.name))
            target.lose_health(self.level)

class GrassType(Pokemon):
    def __init__(self, *args, **kwargs):
        super(GrassType, self).__init__(*args, **kwargs)

#determines the effectiveness of an attack against a given target
    def attack(self, target):
        if self.ko_status == True:
            print('This Pokemon has been knocked out and can no longer attack!')
        elif self.type == 'Grass' and target.type == 'Water':
            print('{} used a super effective attack!'.format(self.name))
            target.lose_health(self.level * 2)
        elif self.type == 'Grass' and target.type == 'Fire':
            print('{}\'s attack was not very effective...'.format(self.name))
            target.lose_health(self.level / 2)
        else:
            print('{} attacks {}.'.format(self.name, target.name))
            target.lose_health(self.level)

class Trainer:
    def __init__(self, name, potion_count, current_active_pokemon, pokemon_list):
        self.name = name
        self.potion_count = potion_count
        self.current_active = current_active_pokemon
        self.pokemon = pokemon_list

#restores health to target pokemon
    def use_potion(self, target):
        updated_hp = target.currenthp
        if target.maxhp < (target.currenthp + 20):
            target.currenthp = target.maxhp
            target.gain_health(target.maxhp - target.currenthp)
        else:
            target.gain_health(20)

#targets another trainer, finding current active pokemon for both trainers
    def attack(self, target):
        attacking_pokemon = self.pokemon[self.current_active]
        defending_pokemon = target.pokemon[target.current_active]
        attacking_pokemon.attack(defending_pokemon)

    def switch_pokemon(self, input):
        if input in self.pokemon:
            if input.ko_status == True:
                print('You cannot switch to a knocked out Pokemon!')
            else:
                new_pokemon_index = self.pokemon.index(input)
                self.current_active = new_pokemon_index
                print('{} brought out {}!'.format(self.name, self.pokemon[self.current_active].name ))
        else:
            print('You do not have that Pokemon!')

#creates the initial pokemon and trainers to test
squirtle = WaterType('Squirtle', 4, 'Water', 35, 35, 0)
charmander = FireType('Charmander', 4, 'Fire', 35, 35, 0)
bulbasaur = GrassType('Bulbasaur', 4, 'Grass', 35, 35, 0)
ash = Trainer('Ash', 4, 0, [squirtle])
gary = Trainer('Gary', 4, 0, [charmander])


#have the trainers attack each other for testing
#Can also use tests for healing, reviving, switching, etc. 
ash.attack(gary)
gary.attack(ash)
