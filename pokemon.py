class Pokemon:
    def __init__(self, name, level, element_type, max_hp, current_hp, ko= False):
        self.name = name
        self.level = level
        self.type = element_type
        self.maxhp = max_hp
        self.currenthp = current_hp
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

        elif self.type == 'Water' and target.type == 'Fire':
            print('{} used a super effective attack!'.format(self.name))
            target.lose_health(self.level * 2)

        elif self.type == 'Water' and target.type == 'Grass':
            print('{}\'s attack was not very effective...'.format(self.name))
            target.lose_health(self.level / 2)

        elif self.type == 'Water' and target.type == 'Water':
            print('{} attacks {}.'.format(self.name, target.name))
            target.lose_health(self.level)

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

    def use_potion(self, target):
        updated_hp = target.currenthp
        if target.maxhp < (target.currenthp + 20):
            target.currenthp = target.maxhp
            target.gain_health(target.maxhp - target.currenthp)
        else:
            target.gain_health(20)

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

squirtle = Pokemon('Squirtle', 4, 'Water', 35, 35)
charmander = Pokemon('Charmander', 4, 'Fire', 35, 35)
ash = Trainer('Ash', 4, 0, [squirtle])
gary = Trainer('Gary', 4, 0, [charmander])


#print(gary.pokemon[gary.current_active].currenthp)
ash.attack(gary)
gary.attack(ash)
