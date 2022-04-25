"""
Main file containg core of the game. This mode is responsible
for creating plotter and controlling pygame
"""
import sys
import argparse
from datetime import datetime
import itertools as itools
import pygame
from matplotlib import pyplot as plt
from population import Population

def create_plotter(keys, healthy, infected, sick):
    """
    Function creates plotter based on given arguments

    Parameters
    ----------
    keys : list
        list containing datetime variables. It will be used to
        show changes in numbers of sick overtime
    healthy : list
        list containing number of healthy people in each time tick
    infected : list
        list containing number of infected people in each time tick
    sick : list
        list containing number of sick people in each time tick

    """
    plt.plot(keys, healthy, 'o-', label="Zdrowi", markersize=3)
    plt.plot(keys, infected, 'o-', label="Zarażeni", markersize=3)
    plt.plot(keys, sick, 'o-', label="Chorzy", markersize=3)
    plt.legend()
    plt.title(label="Rozprzestrzenianie się choroby")
    plt.xticks(rotation=30, fontsize='xx-small', horizontalalignment='right')
    return plt

def text_objects(screen, text, position):
    """
    Function creates text whichi will be shown over buttons
    Parameters:
    -----------
    screen : object
        it reprsents display screen, needed to add something on top of it
    text : string
        text we woould like to show on our button
    position : tuple
        tuple representing x and y, should it be center of button
    """
    font = pygame.font.Font("freesansbold.ttf", 20)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (position[0], position[1])
    screen.blit(text_surface, text_rect)

def draw_menu(screen, mouse):
    """
    Function draws button whichi will be shown at the end of simulation
    parameters:
    ----------
    screen : object
        display screen of aplication we want do draw on
    mouse : tuple
        position of mouse represented by tuple with x and y coordinates
    """
    button_col = (255, 255, 203)
    button_col_hover = ((255, 255, 153))

    if 320 + 160 > mouse[0] > 320 and 150 + 80 > mouse[1] > 150:
        pygame.draw.rect(screen, button_col_hover, (320, 150, 160, 80))
    else:
        pygame.draw.rect(screen, button_col, (320, 150, 160, 80))
    if 320 + 160 > mouse[0] > 320 and 550 + 80 > mouse[1] > 550:
        pygame.draw.rect(screen, button_col_hover, (320, 550, 160, 80))
    else:
        pygame.draw.rect(screen, button_col, (320, 550, 160, 80))

    # Create text
    text_objects(screen, "Zakończ", (400, 190))
    text_objects(screen, "Pokaż wykres", (400, 590))

def draw_person(screen, person, radius):
    """
    Draws person object based on its object and radius from
    Population class.
    Parameters
    ----------
    person : Person object
        object containing informations about localisation
    radius : int
        value describing size of circles
    """
    colour = person.obj_colour
    x_cor = person.x_coordinate
    y_cor = person.y_coordinate

    pygame.draw.circle(screen, colour, (x_cor, y_cor), radius)

def validate_arguments(args):
    """
    Function validates data send by user from parser
    Function checks if data mets conditions otherwise rise an exception

    Parametes:
    ----------
    args : namespace
        namespace containing all the data typed by user into terminal.
    """
    # Variables validation
    if args.NO_OF_PPL >= 2 and args.NO_OF_PPL <= 100:
        no_of_ppl = args.NO_OF_PPL
    else:
        message = 'Value of NO_OF_PPL has to be between 1 and 100'
        raise ValueError(args.NO_OF_PPL, message)
    if args.NO_OF_IMMOB >=0 and args.NO_OF_IMMOB < no_of_ppl:
        no_of_imm = args.NO_OF_IMMOB
    else:
        message = ('Value of NO_OF_IMMOB has to be lesser than'
                   'number of all ppl and cant be negative')
        raise ValueError(args.NO_OF_IMMOB, message)
    inc_per = args.INC_PERIOD
    if args.SPEED >= 1 and args.SPEED <= 10:
        speed = args.SPEED
    else:
        message = ('Value of SPEED have to be between 1 and 10')
        raise ValueError(args.SPEED, message)
    return no_of_ppl, no_of_imm, inc_per, speed

def main(arguments):
    """
    Main function, is responsibles for creating population object and
    receiving arguments. From this function all other are called
    """

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
                        'NO_OF_PPL',
                        type = int,
                        default = 2,
                        help = ("Number of people in the simulation"
                                "Only values between 2 - 100 are allowed")
                        )
    parser.add_argument(
                        'NO_OF_IMMOB',
                        type = int,
                        default = 10,
                        help = ("How many people don't move when started"
                                "Value have to be lesser than"
                                "NO_OF_PPL variable")
                        )
    parser.add_argument(
                        'INC_PERIOD',
                        type = float,
                        default = 10,
                        help = "How long infected spread disease in seconds"
                        )
    parser.add_argument(
                        'SPEED',
                        type = int,
                        default = 10,
                        help = ("How fast are objects when started "
                                "Choose value between 1 - Very slow "
                                "to 10 - very vast")
                        )

    # Initialize variables for class
    args = parser.parse_args(arguments[1:])
    no_of_ppl, no_of_imm, inc_per, speed = validate_arguments(args)

    # Initialize the pygame and window properities
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    background_colour = (255, 255, 255)

    # Title and Icon
    # Icons made by Eucalyp https://www.flaticon.com/authors/eucalyp from www.flaticon.com
    pygame.display.set_caption("Symulator choroby")
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)

    # Initialize Population object
    population = Population(no_of_ppl, no_of_imm, speed)

    # Initialize arrays for plotter
    healthy = []
    infected = []
    sick = []
    keys = []

    # Simulation Loop
    running = True
    while running:
        # Initialize data for while loop
        screen.fill(background_colour)
        now = datetime.now()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and population.infected_ppl == 0:
                mouse = pygame.mouse.get_pos()
                if 320 + 160 > mouse[0] > 320 and 150 + 80 > mouse[1] > 150:
                    running = False
                elif 320 + 160 > mouse[0] > 320 and 550 + 80 > mouse[1] > 550:
                    chart = create_plotter(keys,healthy,infected,sick)
                    chart.show()

        for person in population.people_list:
            # Studying health state of person
            status = person.health_state
            if person.is_sick(now, inc_per) and status == 'infected':
                person.change_health_state('sick')
                population.sick_ppl += 1
                population.infected_ppl -= 1

            # Visualization of person object
            person.change_coordinates()
            draw_person(screen, person,population.radius)

        # Creating set of uniqe pairs, required to examinate collisions
        unique_pairs = itools.combinations(population.people_list, 2)

        for pair in unique_pairs:
            if population.check_if_collide(pair):
                population.spread_disease(pair, now)
                population.coordinates_after_collision(pair)

        if population.infected_ppl == 0:
            mouse = pygame.mouse.get_pos()
            draw_menu(screen, mouse)
        else:
            # Updating arrays for plotter
            keys.append(now)
            healthy.append(population.healthy_ppl)
            infected.append(population.infected_ppl)
            sick.append(population.sick_ppl)

        pygame.display.update()


if __name__ == "__main__":
    main(sys.argv)
