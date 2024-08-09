import time, random

class Player:
    def __init__(self, player_race, player_name,player_hp):
        self.player_race = player_race
        self.player_name = player_name
        self.player_hp = player_hp

class Monster:
    
    monsters = {'Rat': 10, 'Wolf': 15}
    
    def __init__(self, monster_name, monster_hp):
        self.monster_name = monster_name
        self.monster_hp = monster_hp

    @classmethod
    def spawn_monster(cls):
        random_choice = random.choice(list(cls.monsters.keys()))
        monster_hp = cls.monsters[random_choice]                    # random_choise = string with name rat or wolf (keys)
        return cls(random_choice, monster_hp)
    
    def __str__(self):
        return f"A {self.monster_name} with {self.monster_hp} HP appears!"

class Game:
    def __init__(self):
        self.running = True
        self.player = None
    
    def start_game(self):
        player_race,player_name = input("Race?!"), input("Name?!")
        time.sleep(1)
        self.player = Player(player_race, player_name,100)
        print(f"{self.player.player_name} the {self.player.player_race}!!")
        time.sleep(1)
        print("I like it...")
        
        line,fineline = 80 * '!-', 80 * '-'
        space = 80 * ' '
        
        #loop#
        while self.running: 
            time.sleep(1)
            print(f"{line}\n{space}LEVEL 1\n{line} ")
            time.sleep(2)
            print("... Random events will apear, type 'fight','run' or status'")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            if ans.lower() == "stop":
                self.running = False
                print("Ending the game...")
                time.sleep(1)
            else:
                self.spawn()
                
                
    def turn(self):
        
        while monster.monster_hp != 0: 
            
            print(f"Its your turn, ")
        
    
    def spawn(self):
        monster = Monster.spawn_monster()
        print(monster)
        time.sleep(1)

# Criar e iniciar o jogo
game = Game()
game.start_game()
