from office_space_allocation.person import Person
from office_space_allocation.fellow import Fellow
from office_space_allocation.staff import Staff
from office_space_allocation.livingroom import LivingRoom
import random


class Amity:
    # TODO : Complete definition
    def __init__(self):
        self.all_persons = []
        self.all_rooms = []
        self.allocated_rooms = []

    def add_room(self, new_room):
        """
        Adds ```Room``` new_room to list of all_rooms
        :param ```Room``` new_room
        """
        self.all_rooms.append(new_room)

    def add_person(self, person):
        """
        Adds a new Person to list of persons
        :param: ```Person``` person
        """
        if not isinstance(person, Person):
            raise TypeError("Argument should be of type Person")
        else:
            self.all_persons.append(person)

    def find_room(self, name):
        """
        Find a ```Room``` object using name
        :param name: ```str``` name of the Room to look for
        :return: ```Room``` object if found
        """
        name = name.lower()
        for r in self.all_rooms:
            if name == r.get_name().lower():
                return r
        raise ValueError(name + " not found!")

    def allocate_room(self, person):
        """
        Allocates a room to ```Person``` person.

        This is done randomly.
        :param person: ```Person``` to allocate room
        :return: room : ```Room``` allocated , if possible
        """
        if isinstance(person, Fellow):
            # raise exception if there are no rooms
            if len(self.all_rooms) < 1:
                raise IndexError("There are no available rooms")
            else:
                rm = random.choice(self.all_rooms)
                rm.add_person(person)
                self.allocated_rooms.append(rm)
                return rm
        elif isinstance(person, Staff):
            # allocate only livingrooms
            livingrooms = [lr for lr in self.all_rooms if isinstance(lr, LivingRoom)]
            if len(livingrooms) < 1:
                raise IndexError("There are no more LivingRooms to allocate")
            else:
                rm = random.choice(livingrooms)
                rm.add_person(person)
                self.allocated_rooms.append(rm)
                return rm
        else:
            raise TypeError("Person argument must be of type Staff or Fellow")
