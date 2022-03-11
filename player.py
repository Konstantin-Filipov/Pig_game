"""Player class"""
class Player:
    score = 0
    score_turn = 0
    name = None
    player_counter = 1
    index = 0

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



    #def sort(player_record_list):
        #this method should sort the players' scores.
    #    for item in player_record_list:
    #        item
