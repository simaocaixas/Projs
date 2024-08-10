import time,random, math

class Player:
    
    def __init__(self,Player_hp,Player_atk,Player_def,Player_st,Player_lm):
        
        self.Player_hp = Player_hp
        self.Player_atk = Player_atk 
        self.Player_def = Player_def
        self.Player_st = Player_st 
        self.Player_sh = Player_lm
        self.Player_inv = []
        

    def Show_status(self):
        Status = {
            'Health': self.Player_hp,
            'Attack': self.Player_atk,
            'Defence': self.Player_def,
            'Stamina': self.Player_st,
            'Shards': self.Player_sh
        }
        
        Status_line = "+" + "-"*43 + "+"
        spacing = 20
        
        print(Status_line)
        print("|{:^40}|".format("🟢 PLAYER STATUS 🟢"))
        print(Status_line)
        
        for key, value in Status.items():
            print(f"| {key:<{spacing}}: {value:>{spacing-2}}  |")
        
        print(Status_line)
       
            
    def Change_status(self, What_change, How_much):
        if What_change == 'Health':
            self.Player_hp += How_much
        elif What_change == 'Attack':
            self.Player_atk += How_much
        elif What_change == 'Defence':
            self.Player_def += How_much
        elif What_change == 'Stamina':
            self.Player_st += How_much
        elif What_change == 'Shards':
            self.Player_sh += How_much
                
class Monster:

    def __init__(self, Monster_name, Monster_hp, Monster_attack, Monster_defense):
        self.Monster_name = Monster_name
        self.Monster_hp = Monster_hp
        self.Monster_attack = Monster_attack
        self.Monster_defense = Monster_defense

    def take_damage(self, damage):
        self.Monster_hp -= damage
        if self.Monster_hp < 0:
            self.Monster_hp = 0
            
    def is_alive(self):
        
        return self.Monster_hp > 0
    
    def monster_atk(self,player):
        
        damage = random.randint(1, self.Monster_attack)
        print(f"{self.Monster_name} attacks with {damage} damage!")
        player.Player_hp -= damage
        if player.Player_hp < 0:
            player.Player_hp = 0            
                
class Game:
    
    def waiting_lines(self):
        print("Loading...")
        time.sleep(1)
        print("|▇      | 20%")
        time.sleep(1)
        print("|▇▇    | 40%")
        time.sleep(1)
        print("|▇▇▇  | 60%")
        time.sleep(1)
        print("|▇▇▇▇| 100%")
        time.sleep(1)
    
    def create_monster(self):
        names = ['Goblin', 'Orc', 'Dragon']
        name = random.choice(names)
        hp = random.randint(5, 10)
        attack = random.randint(1, 3)
        defense = random.randint(1, 2)
        return Monster(name, hp, attack, defense)
        
    def roll_d20(self):
        return random.randint(1, 20) 
        
    def add_to_bag(self, player, items):
        for item in items:
            player.Player_inv.append(item)
                

    def open_bag(self, player):
        if len(player.Player_inv) == 0:
            print("The inventory is empty!")
        else:
            print("Your inventory contains:")
            time.sleep(1)
            for item in player.Player_inv:
                print(f" - {item}")
                time.sleep(1)
    
    def level_1(self,player):
        
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print("~~~~~~~~~~~~~~~~~~~~~~~~🧙 Level 1 🧙 ~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(1)
        print("~~~~~~~~~~~~~~~~~~Eldoria: The Arcane Citadel~~~~~~~~~~~~~~~~~")
        time.sleep(1)
        print('.')
        time.sleep(1)
        print("-> Welcome to Eldoria, the jewel of the Arcane Realm")
        time.sleep(1)
        
        interaction = input("-> Press 'b' to check your bag")
        time.sleep(1)
        
        self.add_to_bag(player,['Molten Cheese 🧀','Healing Potion 🧪'])
        self.open_bag(player)

        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('From now one you will be on your own!')
        time.sleep(1)
        print('Defeating 4 enemys will grand you acess to Level 2!')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        monster = self.create_monster()
        print(f"A {monster.Monster_name} with {monster.Monster_hp} HP is looking at you!")
        time.sleep(1)
        
        while monster.is_alive() and player.Player_hp > 0:
                time.sleep(1)
                print("\nYour turn:")
                time.sleep(1)
                action = input("Do you want to attack or use an item? (attack/item): ")
                if action.lower() == 'attack':
                    damage = random.randint(1, player.Player_atk)
                    time.sleep(1)
                    print(f"You attack the {monster.Monster_name} for {damage} damage!")
                    monster.take_damage(damage)
                    if monster.is_alive():
                        monster.monster_atk(player)
                        time.sleep(1)
                        print(f"Your HP: {player.Player_hp}")
                    else:
                        time.sleep(1)
                        print(f"You have defeated the {monster.Monster_name}!")
                elif action.lower() == 'item':
                    time.sleep(1)
                    print("Using items is not implemented yet.")
                else:
                    time.sleep(1)
                    print("Invalid action. Please choose 'attack' or 'item'.")
            
    def nice_pause(self):
        
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')

        
    def start_game(self):
        self.gamerunning = True

        print("☆☆ Welcome to TXTRPG ☆☆")
        time.sleep(1)
        self.nice_pause()
        time.sleep(1)
        print("Lest start by creating your character")
        time.sleep(1)
        self.nice_pause()
        symbols = ['❤️️','⚔️','💪','💧','💰']
        Status_str = ['Health','Attack','Defence','Stamina','Shards']
        player = Player(0,0,0,0,0)
        for i in range(0,5):
            print(f"<Press 'r' to roll for {Status_str[i]}>")
            Terminal_roll_interaction = input()
            rolled = self.roll_d20()
            player.Change_status(Status_str[i],rolled)
            time.sleep(0.7)
            print(f"{symbols[i]} You rolled {rolled} {Status_str[i]} points! {symbols[i]}") 
            time.sleep(1)
            self.nice_pause()

        print("Good!")
        time.sleep(1)
        print("Now lets see your character sheet.")
        time.sleep(2)
        self.waiting_lines()
        player.Show_status()
        time.sleep(2)
        self.level_1(player)
        
        

game = Game()
game.start_game()
            
    
    
    
    
    
    
    
