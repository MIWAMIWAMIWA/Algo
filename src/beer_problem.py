"""
this is Solution to the beer problem from algo course in IOT
the beer problem is actually Set cover problem, which belongs to NP-problems
which that it have no other solution than the brute force which will have O(b!)
 b is number of possible beers
"""


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


def set_cover_beer(beer_file, output_file):
    """
    brute force solution to a NP problem,there is nothing we can do
    :return:
    """
    matrix_of_beer, final_beers = string_to_matrix(reading_string(beer_file))
    beers_aff, needed_users = reformat_beer(matrix_of_beer, final_beers)

    while needed_users:
        best_beer = None
        users_covered = set()
        for beer, users in beers_aff.items():
            covered = needed_users & users
            if len(covered) > len(users_covered):
                best_beer = beer
                users_covered = covered
        needed_users -= users_covered
        final_beers.add(best_beer)
    write_beer(final_beers, output_file)
