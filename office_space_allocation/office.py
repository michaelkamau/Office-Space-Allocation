from office_space_allocation.room import Room
from office_space_allocation.fellow import Fellow
from office_space_allocation.utilities import RoomFullError


class Office(Room):
    def __str__(self):
        return "Office: {}".format(self.get_name())

    def add_person(self, person):
        """
        Adds Person ```person``` to the list of occupants of the Office room
        """
        # Check if room is full
        if self.can_accept_occupants():
            self.occupants.append(person)
        else:
            raise RoomFullError("Room is full!")

    def can_accept_occupants(self):
        return self.get_occupants() < 7

# TODO: complete definition of this class
