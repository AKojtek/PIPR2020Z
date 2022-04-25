"""
This module defines Person class which represents single entity
during simulation process.
"""
from datetime import datetime, timedelta
import math
import random

class Person:
    """
    A class used to represent single entity of simulation.

    ...

    Attributes
    ----------
    x_coordinate : int
        defines a x coordinate of object, thanks to this value program decides where
        Person entity should be drawn on x axis
    y_coordinate : int
        defines a y coordinate of object, thanks to this value program decides where
        Person entity should be drawn on y axis
    health_state : string
        defines how object reacts when collides whith another Person object. Can be
        in three states:
        'healthy' : object can be infected but doesn't infect other objects himself
        'infected': object infects other objects, after certain amount of time
                    eneters 'sick' state.
        'sick'    : object can't be infected or infect other objects
    vector_x      : defines change of x coordinate in each frame during simulation
    vector_y      : defines change of y coordinate in each frame during simultaion
    obj_colour : defines colour which will represent this Person state during
                   simulation
    adjust : defines by how much speed given by user will be divided to adjust it
             to screen size

    Methods
    -------
    generate_vector(movement_speed)
        generates vector which is used at the start of the simulation by Person
    change_health_state(status, timestamp)
        changes status of Person and marks when he became infected
    change_coordinates()
        changes values of x and y coordinated based on vector_x and vector_y
    is_sick(now, inc_per)
        checks if person is sick or still infected. Compares marked time
        of infection with now and period of incubation


    """
    def __init__(self,  x_y_cor):
        """
        Parameters
        ----------
        speed : int
            starting speed of person
        x_y_cor : tuple of ints
            describes starting center of circle
        """

        # Initialization of starting postion of object
        self.x_coordinate = x_y_cor[0]
        self.y_coordinate = x_y_cor[1]

        # Initialization of starting health status
        self.health_state = 'healthy'
        self.obj_colour = (0,255,0)
        #self.obj_image = 'images/healthy'
        self.when_infected = datetime.now()

        # Initialization vectores of object
        self.speed = 0
        self.vector_x = 0
        self.vector_y = 0

        # Value to adjust movement speed as 10 would mean 10 px pertick
        # What can cause problems with balls display
        self.adjust = 15

    def random_vector(self,speed):
        """ Generate random value from 0.1 to speed - 0.1 """
        return round(random.uniform(0.1,speed - 0.1), 1)

    def generate_vector(self, movement_speed):
        """
        Function determines starting values of vector axes
        Values depends on a movement_speed argument, which describes how
        many pixels ball goes through in a frame
        ---
        Equation:
        pow(movement_speed,2) = pow(vector_x,2) + pow(vector_y,2)
        """

        self.speed = movement_speed
        movement_speed = pow(movement_speed, 2)

        # Generates random value for x axis
        self.vector_x = self.random_vector(movement_speed)

        self.vector_y = movement_speed - self.vector_x
        self.vector_x = math.sqrt(self.vector_x)
        self.vector_x = self.vector_x / self.adjust
        self.vector_y = math.sqrt(self.vector_y)
        self.vector_y = self.vector_y / self.adjust
        if bool(random.getrandbits(1)):
            self.vector_x = self.vector_x * -1
        if bool(random.getrandbits(1)):
            self.vector_y = self.vector_y * -1

    def change_health_state(self, status, timestamp = 0):
        """
        Changes image and health status of object
        parametrs
        health_state : str
            There are 3 states:
            'healthy'
            'infected'
            'sick'
        timestamp : int
            When person got infected.
            Default is 0.
        """
        if status == 'infected':
            self.health_state = 'infected'
            self.obj_colour = (255,0,0)
            self.when_infected = timestamp
        elif status == 'sick':
            self.health_state = 'sick'
            self.obj_colour = (0,0,0)

    def change_coordinates(self):
        """
        Method changes values of x and y coordinates of
        this object
        """
        if self.x_coordinate <= 8 or self.x_coordinate >= 792:
            self.vector_x = self.vector_x * -1
        if self.y_coordinate <= 8 or self.y_coordinate >= 792:
            self.vector_y = self.vector_y * -1
        self.x_coordinate += self.vector_x
        self.y_coordinate += self.vector_y

    def is_sick(self, now, inc_per):
        """
        Method checks if person became sick already after
        infection

        Parameters
        ----------
        now : datetime
            Current date time
        inc_per : int
            value in seconds representing how long entity should be sick

        Returns
        -------
        True or False depending on datetime comparison.
        """
        seconds = timedelta(seconds=inc_per)
        if now - self.when_infected > seconds:
            return True
        return False
