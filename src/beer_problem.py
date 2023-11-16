"""
this is Solution to the beer problem from algo course in IOT
the beer problem is actually Set cover problem, which belongs to NP-problems
which that it have no other solution than the brute force which will have O(b!)
 b is number of possible beers
"""
from itertools import combinations


def reading_string(beer_file):
    """
    reads string input from file and returns it as string
    :return:
    """
    with open(beer_file, "r", encoding="utf-8") as file:
        data = file.read()
    return data


def string_to_matrix(string):
    """
    :returns matrix where row is user and indexes of preferences of beer:
    """
    final_matrix = []
    row_arr = []
    must_have_beers = set()
    for i in string:
        if i != " ":
            if i == "Y":
                row_arr.append(1)
            else:
                row_arr.append(0)
        else:
            final_matrix.append(row_arr)
            if sum(row_arr) == 1:
                must_have_beers.add(row_arr.index(1))
            row_arr = []
    final_matrix.append(row_arr)
    if sum(row_arr) == 1:
        must_have_beers.add(row_arr.index(1))

    return final_matrix, must_have_beers


def reformat_beer(matrix_of_beer, final_beers):
    """
    reformat beers and users from matrix to dictionaries for a better runtime
    and also already write beers to answer,if there users that love only one type of
    beer, and also not add to needed_users users that love that type of beer, because we
    will anyway add this type of beer, and we can 'forget' about them

    this function returns dict where key is beer and value is set of users who love that type
    of beer AND returns also set of users for which we need to choose beer
    """
    beers_affiliation = {}
    needed_users = set()
    for user_id in range(len(matrix_of_beer)):
        is_needed = 1
        for beer_id in final_beers:
            if matrix_of_beer[user_id][beer_id] == 1:
                is_needed = 0
                break
        if is_needed:
            needed_users.add(user_id)
            for beer_id in range(len(matrix_of_beer[0])):
                if matrix_of_beer[user_id][beer_id]:
                    if beer_id not in beers_affiliation:
                        beers_affiliation[beer_id] = set()
                    beers_affiliation[beer_id].add(user_id)
    return beers_affiliation, needed_users


def write_beer(final_beers, output_file):
    """
    writes solution to the file
    :return:
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(final_beers))


def generate_combinations(input_set):
    """
    Generates all possible combinations of elements in a set.

    """

    def helper(current_combination, remaining_elements, all_combinations):
        if not remaining_elements:
            all_combinations.append(tuple(current_combination))
        else:
            helper(current_combination + [remaining_elements[0]], remaining_elements[1:], all_combinations)
            helper(current_combination, remaining_elements[1:], all_combinations)

    all_combinations = []
    helper([], list(input_set), all_combinations)
    return all_combinations


def set_cover_beer(beer_file, output_file):
    """
    brute force solution to a NP problem,there is nothing we can do
    :return:
    """

    matrix_of_beer, final_beers = string_to_matrix(reading_string(beer_file))
    beers_aff, needed_users = reformat_beer(matrix_of_beer, final_beers)
    beers_comb = generate_combinations(set(beers_aff.keys()))
    best_len = None
    best_comb = None
    for comb in beers_comb:
        needed = needed_users.copy()
        for beer in comb:
            needed -= beers_aff[beer]
        if len(needed) == 0:
            if best_len is None or best_len > len(comb):
                best_len = len(comb)
                best_comb = comb
    final_beers.update(set(best_comb))
    write_beer(final_beers, output_file)
