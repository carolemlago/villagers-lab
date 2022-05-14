# """Functions to parse a file containing villager data."""
# def open_file(file_name):

#     opened_file = open(file_name)
#     for line in opened_file:
#         words = line.split("|")
#         species_name = words[0]
#         species = words[1]
#         personality = words[2]
#         catch_phrase = words[3]

#     return opened_file

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    set_species = set()

    opened_file = open(filename)

    for line in opened_file:
        words = line.split("|")
        # species_name = words[0]
        species = words[1]
        set_species.add(species)
        # personality = words[2]
        # catch_phrase = words[3]

    # species = set(list_species)

    # TODO: replace this with your code

    return set_species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villagers_file = open(filename)

    villagers = []
        
    for line in villagers_file:
        words = line.split("|")
        villagers_name = words[0]
        species = words[1]
        if search_string == species:
            villagers.append(villagers_name)
        else:
            villagers.append(villagers_name)
        # personality = words[2]
        # catch_phrase = words[3]

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    opened_file = open(filename)
    hobby_animals = [fitness_list,play_list, education_list, fashion_list, nature_list, music_list]
    fitness_list = []
    play_list = []
    education_list = []
    fashion_list = []
    nature_list = []
    music_list = []

    for line in opened_file:
        words = line.split("|")
        villagers_name = words[0]
        # species = words[1]
        # list_species.append(species)
        hobby = words[3]
        # catch_phrase = words[4]
        if hobby == "Play":
            play_list.append(villagers_name)
        elif hobby == "Education":
            education_list.append(villagers_name) 
        elif hobby == "Fashion":
            fashion_list.append(villagers_name)
        elif hobby == "Nature":
            nature_list.append(villagers_name)
        elif hobby == "Music":
            music_list.append(villagers_name)
        elif hobby == "Fitness":
            fitness_list.append(villagers_name)    

    return hobby_animals


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    opened_file = open(filename)

    for line in opened_file:
        words = line.split("|")
        words_tuple = tuple(words)
        all_data.append(words_tuple)

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    opened_file = open(filename)

    for line in opened_file:
        words = line.split("|")
        vill_name = words[0]
        # species = words[1]
        # set_species.add(species)
        # personality = words[2]
        catch_phrase = words[4]
        if vill_name == villager_name:
            return catch_phrase
        else:
            return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
