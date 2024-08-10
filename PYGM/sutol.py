import time,random, math

class Player:
    
    def __init__(self,Player_hp,Player_atk,Player_def,Player_st,Player_lm):
        
        self.Player_hp = Player_hp
        self.Player_atk = Player_atk 
        self.Player_def = Player_def
        self.Player_st = Player_st 
        self.Player_sh = Player_lm
        
    def Show_status(self):
        
        Status = {'Health':self.Player_hp,'Attack': self.Player_atk,'Defence': self.Player_def,'Stamina': self.Player_st,'Shards': self.Player_sh}
        Status_line,i = 40 * "|-",0
        
        print(Status_line)
        for i in Status:
            print(f"| {i}: {Status[i]}")
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
    def roll_d20(self):
        return random.randint(1, 20) 
        
    def start_game(self):
        self.gamerunning = True

        print("☆☆ Welcome to TXTRPG ☆☆")
        time.sleep(2)
        print("Lest start by creating your character")
        time.sleep(2)

        Status_str = ['Health','Attack','Defence','Stamina','Shards']
        player = Player(0,0,0,0,0)
        for i in range(0,5):
            print(f"<Press 'r' to roll for {Status_str[i]}>")
            Terminal_roll_interaction = input()
            rolled = self.roll_d20()
            player.Change_status(Status_str[i],rolled)
            print(f"❀ You rolled {rolled} {Status_str[i]} points! ❀") 
            time.sleep(2)

        time.sleep(1)
        print("Good!")
        time.sleep(1)
        print("Now lets see your character sheet.")
        self.waiting_lines()
        time.sleep(1)
        player.Show_status()

game = Game()
game.start_game()
            
    
    
    
    
    
    
    
