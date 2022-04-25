from casino import Player, Casino

def main():
    new_player = Player(input("Podaj imię gracza "))
    list_of_players = [new_player]
    do_you = input("Czy chcesz dodać nowego gracza? (t/n) ")
    while do_you == 't':
        new_player = Player(input("Podaj imię gracza "))
        list_of_players.append(new_player)
        do_you = input("Czy chcesz dodać nowego gracza? (t/n) ")
    game = Casino(list_of_players)
    game.play_game()
    print("Dziękuję za grę!")


if __name__ == "__main__":
    main()
