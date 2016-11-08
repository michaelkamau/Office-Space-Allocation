class Room:
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
