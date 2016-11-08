from office_space_allocation.room import Room
from office_space_allocation.fellow import Fellow


class Office(Room):
    def add_person(self, person):
        """
        Adds Person ```person``` to the list of occupants of the Office room
        """
        self.occupants.append(person)

    def can_accept_occupants(self):
        return self.get_occupants() <= 6

# TODO: complete definition of this class
