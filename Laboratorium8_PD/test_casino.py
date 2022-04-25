import random
import pytest
from casino import Player, Casino
from casino import PlayerWithoutName, DiceLayoutWasNotSet, WrongObjectInList

def test_new_player():
    new_player = Player("Grzegorz")
    assert new_player.get_player_name() == "Grzegorz"


def test_new_player_number():
    new_player = Player(12)
    assert new_player.get_player_name() == "12"



def test_new_player_empty_name():
    with pytest.raises(PlayerWithoutName):
        new_player = Player()


def test_set_dice_values():
    new_player = Player("Test")
    new_player.set_dice_values([1,2,3,4])
    assert new_player.get_dice_values() == [1,2,3,4]


def test_set_dice_values_too_long():
    new_player = Player("Test")
    with pytest.raises(ValueError):
        new_player.set_dice_values([1,2,3,4,5])


def test_get_score_of_even():
    new_player = Player("Tet")
    new_player.set_dice_values([6,6,6,2])
    assert new_player.get_score_even_odd() == 22


def test_get_score_of_odd():
    new_player = Player("Tet")
    new_player.set_dice_values([5,5,3,3])
    assert new_player.get_score_even_odd() == 19


def test_get_score_of_not_even_nor_odd():
    new_player = Player("Tet")
    new_player.set_dice_values([5,2,5,1])
    assert new_player.get_score_even_odd() == 0


def test_get_score_of_pairs():
    new_player = Player("Tet")
    new_player.set_dice_values([2,2,3,1])
    assert new_player.get_score_repeated_dices() == 4


def test_get_score_of_more_pairs():
    new_player = Player("Tet")
    new_player.set_dice_values([2,2,4,4])
    assert new_player.get_score_repeated_dices() == 8


def test_get_score_triple():
    new_player = Player("Tet")
    new_player.set_dice_values([3,3,3,1])
    assert new_player.get_score_repeated_dices() == 12


def test_get_score_quadruple():
    new_player = Player("Tet")
    new_player.set_dice_values([6,6,6,6])
    assert new_player.get_score_repeated_dices() == 36


def test_get_score_both():
    new_player = Player("Tet")
    new_player.set_dice_values([6,6,6,2])
    assert new_player.get_score() == 24


def test_get_score_both2():
    new_player = Player("Tet")
    new_player.set_dice_values([5,3,5,3])
    assert new_player.get_score() == 19


def test_create_casino():
    new_player = Player("Tet")
    new_player2 = Player("Test")
    new_casino = Casino([new_player,new_player2])
    assert new_casino.get_players() == [new_player,new_player2]


def test_create_casino_wrong_object():
    with pytest.raises(WrongObjectInList):
        new_casino = Casino(["str"])


def test_add_to_casino():
    new_player = Player("Tet")
    new_player2 = Player("Test")
    new_casino = Casino([new_player,new_player2])
    new_player3 = Player("Testa")
    new_casino.add_players(new_player3)
    assert new_casino.get_players() == [new_player,new_player2,new_player3]
