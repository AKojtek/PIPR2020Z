"""
Module generate population based on argument provided with
"""
from datetime import datetime
import random
import math
import numpy as np
from person import Person

class Population:
    """
    Class used to represent subjects

    ...

    Attributes
    ----------
    no_of_subjects : int
        This value determines starting number of subjects during the test
    no_of_immobile : int
        This value describes number of not moving cases when simulation starts
    movement_speed : int
        This value defines starting movement speed of every object
        during simulation
    number_error : bool
        value checks if requirment number of subjects was met
        if not will be set as True
    people_list : list
        list containing all the test subjects during the simulation
    healthy_ppl : int
        number of healthy people
    infected_ppl : int
        number of infected people, people who can spread the disease
    sick_ppl : int
        number of sick people, they were infected but do not spread it anymore

    Methods
    -------
    check_if_collide(pair)
        compares x and y values of objects stored in pair, based on that decides
        whether objects collide or not
    spread_disease(pair, now)
        Checks if someone from the pair is infected, if yes marks time of infection
        and spreads disease
    coordinates_after_collison(pair)
        Method calculates new vectors for Person objects.
    generate_coordinates()
        generates random set of unique x and y values for future circles

    """

    def __init__(self, number, immobile_no, speed):
        """
        Parameters
        ----------
        number : int
            number of subjects during simulation
        speed : int
            movement speed of people during simulation
        immobile_no : int
            number of not moving objects on start of the simulation
        """
        self.radius = 8

        #self.incubation_period = time
        self.no_of_subjects = number
        self.no_of_immobile = immobile_no
        self.movement_speed = speed
        self.number_error = False

        # Generate list of x,y which represents center of each circle
        centers_list = self.generate_coordinates()

        # Generate list of test subjects
        self.people_list = []
        for center in centers_list:
            person = Person(center)
            self.people_list.append(person)

        for person in self.people_list[: - immobile_no]:
            person.generate_vector(speed)

        # Initialize one person as infected
        self.people_list[0].change_health_state('infected', datetime.now())

        # Initialize variables describing number of cases
        self.healthy_ppl = self.no_of_subjects - 1
        self.infected_ppl = 1
        self.sick_ppl = 0

    def check_if_collide(self, pair):
        """
        Method compares pair of Person objects and decides if they collide
        Parameters
        ----------
        pair : tuple
            stores two objects of class Person

        Returns
        -------
        boolean
            True if objects collide and False otherwise
        """
        x_value = pair[0].x_coordinate - pair[1].x_coordinate
        y_value = pair[0].y_coordinate - pair[1].y_coordinate
        distance = math.hypot(x_value, y_value)
        if distance <= 16:
            return True
        else:
            return False

    def spread_disease(self,pair, now):
        """
        Method compares if pair is build of one infected
        and one healthy person, if this is true, then spreads disease
        Updates numbers of sick and healthy people

        Parameters
        ----------
        pair : tuple
            stores two objects of class Person
        now : datetime
            current time to mark date of infection
        """
        if  (
                pair[0].health_state == 'infected' and
                pair[1].health_state == 'healthy'
            ):
            pair[1].change_health_state('infected', now)
            self.infected_ppl += 1
            self.healthy_ppl -= 1
        elif (
                pair[1].health_state == 'infected' and
                pair[0].health_state == 'healthy'
            ):
            pair[0].change_health_state('infected', now)
            self.infected_ppl += 1
            self.healthy_ppl -= 1



    def coordinates_after_collision(self,pair):
        """
        compares coordinates and vectors of objects stored
        in pair variable and changes values of its vectors
        based on that.
        For calculations uses equations related to elastic
        collision.

        Parameters:
        ----------
        pair : tuple
            stores two objects of class Person

        """

        # Initialize variables of vectors and circle centers
        vec1 = np.array((pair[0].vector_x,pair[0].vector_y))
        vec2 = np.array((pair[1].vector_x,pair[1].vector_y))
        cen1 = np.array((pair[0].x_coordinate,pair[0].y_coordinate))
        cen2 = np.array((pair[1].x_coordinate,pair[1].y_coordinate))

        # Computes new vectors
        dist = np.linalg.norm(cen1 - cen2)**2
        new_vec1 = vec1 - np.dot(vec1-vec2, cen1-cen2) / dist * (cen1 - cen2)
        new_vec2 = vec2 - np.dot(vec2-vec1, cen2-cen1) / dist * (cen2 - cen1)

        pair[0].vector_x = new_vec1[0]
        pair[0].vector_y = new_vec1[1]
        pair[1].vector_x = new_vec2[0]
        pair[1].vector_y = new_vec2[1]

    def generate_coordinates(self):
        """
        Method generates list of x and y values.
        Each pair is checked wheter it overlap or not circle centers
        generated before
        circle radius : value set in init = 8
        distance from box borders have to be at least > that 8 px

        because of that values will be choosen from display size
        - 8px from each side
        x_cor = rand(radius, 800 - radius)
        y_cor = rand(radius, 800 - radius)
        """

        # Initialize empty list of circles
        centers = []

        # Generate pairs of x,y while certain number of centers is not met
        # As this is bruteforce, program will count number of failures
        # and break loop if unable to met given number
        brut_force_protection = 0

        radius = self.radius
        while len(centers) < self.no_of_subjects:
            # Generate random x and y values
            x_cor = random.randint(radius, 800 - radius)
            y_cor = random.randint(radius, 800 - radius)

            is_overlapping = False
            for circle in centers:
                distance = math.hypot(x_cor - circle[0], y_cor - circle[1])
                if distance <= radius * 2:
                    is_overlapping = True
                    break

            if not is_overlapping:
                centers.append((x_cor, y_cor))
            else:
                brut_force_protection += 1

            if brut_force_protection >= 10000:
                break

        if len(centers) < self.no_of_subjects:
            self.number_error = True
            self.no_of_subjects = len(centers)

        return centers
