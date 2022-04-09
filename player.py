"""Player class"""
import dice

class Player:
    score = 0
    score_turn = 0
    name = None
    player_counter = 1
    index = 0
    isCheater = False
    isWiner = False

    def __init__(self, i):
        """Constructor with 'index' parameter"""
        self.index = i

    def setName(self):
        """"set current name of player"""
        print(f"set player{self.index} name:")
        self.name = input()
        print(f"nickname for player{self.index} is set to {self.name}\n")
        return self.name

    def update_score(self, toAdd):
        """Update player's overall score"""
        self.score_turn += toAdd
        self.score = self.score + toAdd
        print(f"Player {self.name} rolled {toAdd}, overall score: {self.score}")

    def isWinner(self):
        if self.score >= 100:
            print(f"\n{self.name} is the first one who reached 100 points!!")
            print(f"{self.name} WON!\n")
            self.isWiner = True
            return True

    def remove_points(self):
        self.score -= self.score_turn
        print(f"{self.name} rolled 1 and lost points from this turn, overall score is {self.score}")
        return self.score

    def cheat(self):
        """roll dice until exceeds 100"""
        self.dice_obj = dice.Dice()
        while self.score < 100:
            rolled = dice.Dice().roll()
            if rolled == 1:
                rolled += 1
            dice.Dice().dice_graph(rolled)
            self.update_score(rolled)

        print("Congrats!!! You won by cheating :0!")
        self.isCheater = True
        return True
