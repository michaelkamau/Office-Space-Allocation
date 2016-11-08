from office_space_allocation.person import Person


class Amity:
    # TODO : Complete definition
    def __init__(self):
        self.all_persons = []

    def add_person(self, person):
        """
        Adds a new Person to list of persons
        :param: ```Person``` person
        """
        self.all_persons.append(person)
