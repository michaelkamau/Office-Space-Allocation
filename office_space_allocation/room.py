from  abc import ABCMeta, abstractmethod
from office_space_allocation.person import Person


class Room(metaclass=ABCMeta):
    # TODO: complete class definition
    def __init__(self, name):
        self.name = name
        self.occupants = []

    def __str__(self):
        pass

    def get_occupants_tuple(self):
        # TODO: Test this
        return tuple(self.occupants)

    def get_occupants(self):
        """
        Fetches the number of occupants in the room
        :return: ```int``` : occupants
        """
        return len(self.occupants)

    def get_name(self):
        """
        Fetches and returns the name of the room, formatted in title case
        :return: ```str``` : name of room
        """
        return self.name.title()

    @abstractmethod
    def can_accept_occupants(self):
        pass

    @abstractmethod
    def add_person(self, person):
        pass

    def remove_person(self, person):
        """
        Fetches, removes and returns a Person from the list of occupants in the Room
        :param person:
        :return: ```Person``` person
        """
        if not isinstance(person, Person):
            raise TypeError("Argument must be of type Person")
        elif person in self.occupants:
            self.occupants.remove(person)
            return person
