import time

class Player:
    def __init__(self, player_race, player_name):
        self.player_race = player_race
        self.player_name = player_name

class Game:
    def __init__(self):
        self.running = True
        self.player = None
    
    def start_game(self):
        print("What...are..you?")
        time.sleep(1)
        player_race = input("<choose between: Human - Orc - Goblin> ")
        time.sleep(1)
        player_name = input("Whats...your..name?!")
        time.sleep(1)
        self.player = Player(player_race, player_name)
        print(f"{self.player.player_name} the {self.player.player_race}!!")
        time.sleep(1)
        print("i like it...")
        
        ## MAIN LOOP ##
        while self.running: 
            time.sleep(1)
            ans = input("<this is an action, type 'stop' to end the game>: ")
            if ans.lower() == "stop":
                self.running = False
    
game = Game()
game.start_game()
