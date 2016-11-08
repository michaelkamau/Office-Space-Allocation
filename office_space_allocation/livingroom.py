from office_space_allocation.room import Room


class LivingRoom(Room):
    def can_accept_occupants(self):
        return self.get_occupants() <= 4

    # complete this class

