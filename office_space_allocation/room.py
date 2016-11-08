from  abc import ABCMeta, abstractmethod


class Room(metaclass=ABCMeta):
    # TODO: complete class definition
    def __init__(self, name):
        self.name = name
        self.occupants = []

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
