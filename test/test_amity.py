import unittest
from office_space_allocation import amity, person, fellow, staff, room, office


class TestAmityClassStructure(unittest.TestCase):
    """
    Tests the class structure of the project
    """

    def test_can_create_amity_instance(self):
        """
        Should be able to create an instance of the Amity class
        """
        self.amity = amity.Amity()
        self.assertIsInstance(self.amity, amity.Amity)

    def test_can_create_person_instance(self):
        """
        Should be able to create an instance of the Person class
        """
        self.person = person.Person("John", "Doe")
        self.assertIsInstance(self.person, person.Person)

    def test_can_create_fellow_instance(self):
        """
        Should be able to create instance of Fellow class
        """
        self.fellow = fellow.Fellow()
        self.assertIsInstance(self.fellow, fellow.Fellow)

    def test_can_create_staff_instance(self):
        """
        Should be able to create instance of the Staff class
        """
        self.staff = staff.Staff()
        self.assertIsInstance(self.staff, staff.Staff)

    def test_can_create_room_instance(self):
        """
        Should be able to create instance of the Room class
        """
        self.room = room.Room()
        self.assertIsInstance(self.room, room.Room)

    def test_can_create_office_instance(self):
        """
        Should be able to create instance of the Office class
        """
        self.office = office.Office()
        self.assertIsInstance(self.office, office.Office)

if __name__ == '__main__':
    unittest.main()
