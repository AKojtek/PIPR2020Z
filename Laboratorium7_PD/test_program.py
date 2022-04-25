import pytest
from program import Polynomial


def test_initiation():
    polynomial = Polynomial([(0,2),(2,3)])
    assert polynomial.get_collection() == [(2,3),(0,2)]


def test_initiation_repeated():
    with pytest.raises(ValueError):
        polynomial = Polynomial([(0,2),(0,3)])


def test_initiation_negative():
    with pytest.raises(ValueError):
        polynomial = Polynomial([(-4,2),(0,3)])


def test_initiation_value0():
    with pytest.raises(ValueError):
        polynomial = Polynomial([(4,2),(1,0)])


def test_initiation_string():
    with pytest.raises(ValueError):
        polynomial = Polynomial([(4,"str"),(1,1)])


def test_str():
    polynomial = Polynomial([(5,2),(2,3)])
    assert polynomial.__str__() == "2x^5+3x^2"


def test_str_negative():
    polynomial = Polynomial([(4,-2),(2,3)])
    assert polynomial.__str__() == "-2x^4+3x^2"


def test_degree():
    a = Polynomial([(4,-2),(2,3)])
    assert a.degree() == 4


def test_degree2():
    a = Polynomial([(4,-2),(6,3)])
    assert a.degree() == 6


def test_coefficient():
    a = Polynomial([(4,-2),(6,3)])
    assert a.coefficient(4) == -2


def test_coefficient2():
    a = Polynomial([(15,-2),(4,3)])
    assert a.coefficient(3) == None


def test_value():
    a = Polynomial([(5,-2),(4,3)])
    assert a.value(2) == -16


def test_value2():
    a = Polynomial([(1,-2),(2,3)])
    assert a.value(4) == 40


def test_add():
    a = Polynomial([(1,2),(2,3)])
    b = Polynomial([(3,4),(4,5)])
    a.add(b)
    assert a.get_collection() == [(4, 5), (3, 4), (2, 3), (1, 2)]

def test_add2():
    a = Polynomial([(1,2),(2,3)])
    b = Polynomial([(3,4),(1,-2)])
    a.add(b)
    assert a.get_collection() == [(3, 4), (2, 3)]


def test_substract():
    a = Polynomial([(1,2),(2,3)])
    b = Polynomial([(3,4),(4,5)])
    a.substract(b)
    assert a.get_collection() == [(4, -5), (3, -4), (2, 3), (1, 2)]


def test_substract2():
    a = Polynomial([(1,2),(2,3)])
    b = Polynomial([(1,2),(4,5)])
    a.substract(b)
    assert a.get_collection() == [(4, -5), (2, 3),]
