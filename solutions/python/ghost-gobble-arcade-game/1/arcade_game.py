# Ex002 Ghost-gobble-arcarde-game
# Project: define four tasks for eating ghosts, scoring, losing and winning.
# # Created: 2026-06-15
# Revision History:
# v1: Initial setup and basic logic.

"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """

    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    Parameters:
        touching_power_pellet (bool): Is the player touching a power pellet?
        touching_dot (bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored or not?

    """

    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player lost the game?

    Possibilities:
    not power_pellet_active (False) and touching_ghost (True) = False
    not power_pellet_active (False) and not touching_ghost (False) = True
    power_pellet_active (True) and touching_ghost (True) = True
    """

    if not power_pellet_active and touching_ghost:
        return True
    else:
        return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """

    return has_eaten_all_dots and not lose(power_pellet_active,touching_ghost)