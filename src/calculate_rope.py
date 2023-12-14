"""
The algorithm based on dynamical programing
"""
import math


def calculate_rope(distance, pillars_list):
    """
    the first parameter is distance between pillars
    second is list of possible heights of pillars for each position
    find length of the longest possible rope through them
    """
    current_top = 0
    current_bottom = 0
    current_height = 0
    for pillar in pillars_list:
        if current_height != 0:  # this only for first pillar
            temp_up_down = current_top + math.sqrt(distance ** 2 + (current_height - 1) ** 2)
            temp_down_down = current_bottom + distance
            temp_up_up = current_top + math.sqrt(distance ** 2 + (abs(current_height - pillar)) ** 2)
            temp_down_up = current_bottom + math.sqrt(distance ** 2 + (pillar - 1) ** 2)
            current_top = max(temp_up_up, temp_down_up)
            current_bottom = max(temp_up_down, temp_down_down)
        current_height = pillar
    return round(max(current_bottom, current_top),2)
