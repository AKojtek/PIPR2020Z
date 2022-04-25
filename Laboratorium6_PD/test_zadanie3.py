import pytest
from zadanie3 import check_if_correct, score_and_average_points_of_student, final_list


def test_check_if_correct_default():
    array = [10,20,30]
    assert check_if_correct(array) == [10,20,30]


def test_check_if_correct_strings():
    array = ['12','13','15']
    assert check_if_correct(array) == [12,13,15]


def test_check_if_correct_wrong_values():
    array = [12,'1o',1267]
    with pytest.raises(ValueError):
        check_if_correct(array)


def test_check_if_correct_wrong_negative():
    array = [-5,-12,-16]
    with pytest.raises(ValueError):
        check_if_correct(array)


def test_score_and_average_points_of_student():
    list_of_scores = [1,3,6,7]
    total_sum = 50
    assert score_and_average_points_of_student(list_of_scores,total_sum) == (17, 34)


def test_score_and_average_points_of_student_overtop():
    list_of_scores = [100,1,1,1]
    total_sum = 10
    with pytest.raises(ValueError):
        score_and_average_points_of_student(list_of_scores,total_sum)


def test_final_list():
    a = [10,20,30]
    b = [("Adam Abacki", [5, 10, 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", [1, 2, 3])]
    assert final_list(a,b) == [("Adam Abacki", 30, 50), ("Basia Babacka", 60, 100), ("Cecylia Cabacka", 6, 10), 32]


def test_final_list2():
    c = [10, 20, 30]
    d = [("Adam Abacki", [5, '1o', 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", 55)]
    assert final_list(c,d) == [('Adam Abacki', None, None), ('Basia Babacka', 60, 100.0), ('Cecylia Cabacka', None, None), 60.0]


def test_final_list_empty_labs():
    a = []
    b = [("Adam Abacki", [5, 10, 15]), ("Basia Babacka", [10, 20, 30]), ("Cecylia Cabacka", [1, 2, 3])]
    with pytest.raises(ValueError):
        final_list(a,b)


def test_final_list_empty_students():
    a = [10,20,30]
    b = []
    with pytest.raises(ValueError):
        final_list(a,b)


def test_final_list_empty_both_lists():
    a = []
    b = []
    with pytest.raises(ValueError):
        final_list(a,b)