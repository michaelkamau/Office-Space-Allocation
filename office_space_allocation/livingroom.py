from office_space_allocation.room import Room
from office_space_allocation.fellow import Fellow
from office_space_allocation.staff import Staff
from office_space_allocation.utilities import InvalidRoomOccupantError


class LivingRoom(Room):
    def add_person(self, person):
        """
        Adds ```Person``` person to the list of occupants of the LivingRoom
        Person should only be of type Fello

        :param : ```Person``` person
        """
        if isinstance(person, Fellow):
            self.occupants.append(person)
        elif isinstance(person, Staff):
            raise InvalidRoomOccupantError("Staff cannot join LivingRooms")

    def can_accept_occupants(self):
        return self.get_occupants() <= 4

    # complete this class

