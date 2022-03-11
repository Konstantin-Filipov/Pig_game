"""Player class"""
import dice

class Player:
    score = 0
    score_turn = 0
    name = None
    player_counter = 1
    index = 0
    isCheater = False

    def __init__(self, i):
        """Constructor with 'index' parameter"""
        self.index = i

    def setName(self, updatedName):
        """"set current name of player"""
        self.name = updatedName

    def update_score(self, toAdd):
        """Update overall score"""
        #This method should update the players score
        self.score = self.score + toAdd

    def cheat(self):
        """roll dice until exceeds 100"""
        self.dice_obj = dice.Dice()
        while self.score < 100:
            rolled = dice.Dice().roll()
            if rolled == 1:
                rolled += 1
            dice.Dice().dice_graph(rolled)
            self.update_score(rolled)
            print(f"Player {self.name} rolled {rolled}, overall score: {self.score}")

        print("Congrats!!! You won by cheating :0!")
        self.isCheater = True



    #def sort(player_record_list):
        #this method should sort the players' scores.
    #    for item in player_record_list:
    #        item
