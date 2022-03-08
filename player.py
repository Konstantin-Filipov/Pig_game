class Player:
    player_record_list = []



    def __init__(self,name,score):
        self.name = name
        self.score = score

    def add_to_list(first_player,second_player):
        Player.player_record_list.append(first_player)
        Player.player_record_list.append(second_player)
        print(Player.player_record_list)

    
    #def update_score(first_player):
       #This method should update the players score
    #   bee = first_player 
        

    #def sort(player_record_list):
        #this method should sort the players' scores.
    #    for item in player_record_list:
    #        item 



first_player = Player('Jane', 0)
second_player = Player('Esther', 23)
Player.add_to_list()



        

   




        
