from person import Person, timedelta
from population import Population
from main import validate_arguments, datetime
import pytest

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def test_person_create():
    person = Person((1,5))
    assert person.health_state == 'healthy'
    assert person.x_coordinate == 1
    assert person.y_coordinate == 5
    assert person.speed == 0


def test_person_create2():
    person = Person((3,2))
    now = datetime.now()
    assert person.when_infected == now
    assert person.x_coordinate == 3
    assert person.y_coordinate == 2


def test_generate_vector(monkeypatch):
    person = Person((1,1))
    def get_vector_x(self,speed):
        return 9
    monkeypatch.setattr('person.Person.random_vector', get_vector_x)
    person.generate_vector(5)
    # sqrt(9) == 3 -> 3/ adjust == 0.20
    assert person.vector_x == 0.20 or person.vector_x == -0.20
    # 25 - 9 = 16 , 4/ adjust == 0.2666666....
    assert person.vector_y == 4/person.adjust or person.vector_y == -4/person.adjust

def test_generate_vector2(monkeypatch):
    person = Person((1,1))
    def get_vector_x(self,speed):
        return 36
    monkeypatch.setattr('person.Person.random_vector', get_vector_x)
    person.generate_vector(10)
    # sqrt(36) == 6 -> 6/ adjust == 0.40
    assert person.vector_x == 0.40 or person.vector_x == -0.40
    # 100 - 36 = 64 , 8/ adjust == 0.53333...
    assert person.vector_y == 8/person.adjust or person.vector_y == -8/person.adjust

def test_change_health_infected():
    person = Person((1,1))
    now = datetime.now()
    person.change_health_state('infected',now)
    assert person.health_state == 'infected'
    assert person.obj_colour == (255,0,0)
    assert person.when_infected == now

def test_change_health_sick():
    person = Person((1,1))
    person.change_health_state('sick')
    assert person.health_state == 'sick'
    assert person.obj_colour == (0,0,0)

def test_change_coordinates():
    person = Person((100,100))
    person.vector_x = 3
    person.vector_y = 4
    person.change_coordinates()
    assert person.x_coordinate == 103
    assert person.y_coordinate == 104

def test_change_coordinates_borderx():
    person = Person((6,100))
    person.vector_x = -3
    person.vector_y = 4
    person.change_coordinates()
    assert person.x_coordinate == 9
    assert person.y_coordinate == 104

def test_change_coordinates_bordery():
    person = Person((150,793))
    person.vector_x = 3
    person.vector_y = 4
    person.change_coordinates()
    assert person.x_coordinate == 153
    assert person.y_coordinate == 789

def test_check_if_still_sick_true():
    person = Person((100,100))
    person.when_infected = datetime.now()
    now = datetime.now() + timedelta(seconds=3)
    inc_per = 2
    assert person.is_sick(now, inc_per)

def test_check_if_still_sick_false():
    person = Person((100,100))
    person.when_infected = datetime.now()
    now = datetime.now() + timedelta(seconds=1)
    inc_per = 3
    assert not person.is_sick(now, inc_per)

def test_create_population():
    pop = Population(5,3,8)
    assert pop.no_of_immobile == 3
    assert pop.no_of_subjects == 5
    assert pop.movement_speed == 8
    assert pop.healthy_ppl == 4
    assert pop.infected_ppl == 1
    assert pop.sick_ppl == 0

def test_generate_coordinates():
    pop = Population(2,1,1)
    centers = pop.generate_coordinates()
    for center in centers:
        assert center[0] >= 8 and center[0] <= 792
        assert center[1] >= 8 and center[1] <= 792

def test_generate_coordinates_error():
    # We set number of objects to a valuse that cannot be met
    pop = Population(4000,1,1)
    pop.generate_coordinates()
    assert pop.number_error

def test_check_if_collide():
    pop = Population(2,0,1)
    person1 = Person((100,100))
    person2 = Person((107,100))
    pop.people_list = [person1,person2]
    assert pop.check_if_collide((person1,person2))

def test_check_if_collide_false():
    pop = Population(2,0,1)
    person1 = Person((100,100))
    person2 = Person((200,100))
    pop.people_list = [person1,person2]
    assert not pop.check_if_collide((person1,person2))

def test_spread_disease():
    person1 = Person((100,100))
    person2 = Person((200,100))
    person1.health_state = 'infected'
    pop = Population(2,0,1)
    pop.people_list = [person1,person2]
    pop.spread_disease((person1,person2),datetime.now())
    assert person2.health_state == 'infected'

def test_spread_disease_sick():
    person1 = Person((100,100))
    person2 = Person((200,100))
    person1.health_state = 'sick'
    pop = Population(2,0,1)
    pop.people_list = [person1,person2]
    pop.spread_disease((person1,person2),datetime.now())
    assert person2.health_state == 'healthy'

def test_spread_disease_sick_infected_sick():
    person1 = Person((100,100))
    person2 = Person((200,100))
    person1.health_state = 'infected'
    person2.health_state = 'sick'
    pop = Population(2,0,1)
    pop.people_list = [person1,person2]
    pop.spread_disease((person1,person2),datetime.now())
    assert person2.health_state == 'sick'

def test_coordinates_after_collision():
    person1 = Person((100,100))
    person2 = Person((100,104))
    person1.vector_x = 3
    person2.vector_x = -4
    person1.vector_y = 4
    person2.vector_y = 3
    pop = Population(2,0,1)
    pop.coordinates_after_collision((person1,person2))
    assert person1.vector_x == 3.0
    assert person1.vector_y == 3.0
    assert person1.x_coordinate == 100
    assert person1.y_coordinate == 100

def test_validate_arguments():
    args = Namespace(
                    NO_OF_PPL = 100,
                    NO_OF_IMMOB = 10,
                    INC_PERIOD = 5,
                    SPEED = 3
                    )
    no_ppl, no_imm, inc, speed = validate_arguments(args)
    assert no_ppl == 100
    assert no_imm == 10
    assert inc == 5
    assert speed == 3

def test_validate_arguments_error1():
    args = Namespace(
                    NO_OF_PPL = 1010,
                    NO_OF_IMMOB = 10,
                    INC_PERIOD = 5,
                    SPEED = 3
                    )
    with pytest.raises(ValueError):
        validate_arguments(args)

def test_validate_arguments_error2():
    args = Namespace(
                    NO_OF_PPL = 10,
                    NO_OF_IMMOB = 10,
                    INC_PERIOD = 5,
                    SPEED = 3
                    )
    with pytest.raises(ValueError):
        validate_arguments(args)

def test_validate_arguments_error3():
    args = Namespace(
                    NO_OF_PPL = 100,
                    NO_OF_IMMOB = 10,
                    INC_PERIOD = 5,
                    SPEED = 33
                    )
    with pytest.raises(ValueError):
        validate_arguments(args)
