from office_space_allocation.room import Room


class Office(Room):
    def can_accept_occupants(self):
        return self.get_occupants() <= 6

# TODO: complete definition of this class
