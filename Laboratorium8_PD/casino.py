import random


class PlayerWithoutName(Exception):
    pass


class DiceLayoutWasNotSet(Exception):
    pass


class WrongObjectInList(Exception):
    pass


class Player:
    def __init__(self,name = None):
        if not name:
            raise PlayerWithoutName("Name was not specified")
        self._name = str(name)
        self._dice_values = None


    def __str__(self):
        return f'This player is called {self._name}'


    def get_player_name(self):
        return self._name


    def set_player_name(self, name):
        self._name = str(name)


    def set_dice_values(self,list_of_dices):
        if len(list_of_dices) != 4:
            raise ValueError("Not valid number of arguments in list")
        for dice in list_of_dices:
            if dice not in range(1,7):
                raise ValueError("Value of dice is wrong! Value can be only from 1 to 6")
        self._dice_values = list_of_dices


    def get_dice_values(self):
        return self._dice_values


    def get_score_even_odd(self):
        layout = self.get_dice_values()
        new_list = [value % 2 == 1 for value in layout]
        if all(new_list):
            return sum(layout)+3
        elif not any(new_list):
            return sum(layout)+2
        return 0


    def get_score_repeated_dices(self):
        layout = self.get_dice_values()
        set_layout = set(layout)
        maximal_value = 0
        for each in set_layout:
            x = layout.count(each)
            if x == 2 and each*2 > maximal_value:
                maximal_value = each*2
            if x == 3 and each*4 > maximal_value:
                maximal_value = each*4
            if x == 4 and each*6 > maximal_value:
                maximal_value = each*6
        return maximal_value


    def get_score(self):
        if self.get_dice_values() is None:
            raise DiceLayoutWasNotSet("You have to make dice rolls first!")
        value_of_even_odd = self.get_score_even_odd()
        value_if_repeated = self.get_score_repeated_dices()
        return max(value_if_repeated,value_of_even_odd)


class Casino:
    def __init__(self,Players = None):
        for each in Players:
            if not isinstance(each, Player):
                raise WrongObjectInList("List contains element that should not be there!")
        self._Players = Players if Players else []


    def get_players(self):
        return self._Players


    def add_players(self,new_player):
        if not isinstance(new_player, Player):
            raise WrongObjectInList("Given object is not playey!")
        self._Players.append(new_player)


    def dice_throw(self):
        dice_values = []
        for _ in range(4):
            dice_values.append(random.randint(1,6))
        return dice_values


    def find_winner(self):
        players = self.get_players()
        winning_score = -1
        winning_player = None
        for Player in players:
            score = Player.get_score()
            if score>winning_score:
                winning_player = Player
                winning_score = score
            elif score == winning_score:
                winning_player = None
        return winning_player


    def winner_of_the_game(self):
        winner = self.find_winner()
        if winner == None:
            return "Runda jest nie rozstrzygnięta!"
        else:
            return f"Rundę wygrywa {winner.get_player_name()} z {winner.get_score()} punktami!"


    def play_round(self):
        if self.get_players() == None:
            return "Nie ma żadnych graczy!"
        else:
            print("Rozpoczynamy rundę!")
            players = self.get_players()
            for each in players:
                each.set_dice_values(self.dice_throw())
            return self.winner_of_the_game()


    def play_game(self):
        print("Zaczynamy!")
        print(self.play_round())
        x = input("Czy chcesz zagrać ponownie? (t/n) ")
        while x == 't':
            new_player = input("Czy chcesz dodać nowego gracza? (t/n) ")
            while new_player == 't':
                new_player = Player(input("Podaj imię/nick nowego gracza "))
                self.add_players(new_player)
                new_player = input("Czy chcesz dodać nowego gracza? (t/n) ")
            print(self.play_round())
            x = input("Czy chcesz zagrać ponownie? (t/n) ")

