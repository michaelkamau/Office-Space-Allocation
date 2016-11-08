import unittest
from office_space_allocation import amity, person, fellow, staff, room, office, livingroom
from office_space_allocation.utilities import InvalidRoomOccupantError


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
        self.fellow = fellow.Fellow("Ken", "Mitch")
        self.assertIsInstance(self.fellow, fellow.Fellow)

    def test_can_create_staff_instance(self):
        """
        Should be able to create instance of the Staff class
        """
        self.staff = staff.Staff("Jack", "Bauer")
        self.assertIsInstance(self.staff, staff.Staff)

    def test_can_create_office_instance(self):
        """
        Should be able to create instance of the Office class
        """
        self.office = office.Office("Krypton")
        self.assertIsInstance(self.office, office.Office)

    def test_can_create_livingroom_instance(self):
        """
        Should be able to create instance of the LivingRoom class
        """
        self.lroom = livingroom.LivingRoom("Bedroom")
        self.assertIsInstance(self.lroom, livingroom.LivingRoom)

    def test_fellow_is_subclass_of_person(self):
        """
        Fellow should be a subclass of the Person class
        """
        self.f1 = fellow.Fellow("Mary", "Jane")
        self.assertIsInstance(self.f1, person.Person)

    def test_staff_is_subclass_of_person(self):
        """
        Staff should be a subclass of the Person class
        """
        self.staff = staff.Staff("King", "Kong")
        self.assertIsInstance(self.staff, person.Person)

    def test_office_is_subclass_of_room(self):
        """
        Office class should subclass Room class
        """
        self.office = office.Office("Oculus")
        self.assertIsInstance(self.office, room.Room)

    def test_livingroom_subclasses_room(self):
        """
        LivingRoom class should subclass Room class
        """
        self.livroom = livingroom.LivingRoom("Bedroom")
        self.assertIsInstance(self.livroom, room.Room)


class TestRoomClass(unittest.TestCase):
    """
    Tests the functionality of Room class, and its subclasses LivingRoom and Office
    """

    def test_office_room_has_zero_occupants_by_default(self):
        """
        By default, a Office room created should have zero occupants
        """
        self.rm = office.Office("Hogwarts")
        self.assertEqual(self.rm.get_occupants(), 0)

    def test_get_name_office_room(self):
        """
        Should return the name of the office room, formatted in title case
        """
        self.rm = office.Office("Quiet room")
        self.assertEqual(self.rm.get_name(), "Quiet Room")

    def test_get_name_livingroom(self):
        """
        Should be able to get name of LivingRoom room, formatted in title case
        """
        self.lvroom = livingroom.LivingRoom("Chillout place")
        self.assertEqual(self.lvroom.get_name(), "Chillout Place")

    def test_can_add_fellow_to_office_room(self):
        """
        Should be able to add fellows to Office room
        """
        self.of = office.Office("New Office")
        self.fel = fellow.Fellow("Mary", "Jane")
        self.of.add_person(self.fel)
        self.assertEqual(self.fel, self.of.occupants[0])

    def test_can_add_fellow_to_livingroom_room(self):
        """
        Should be able to add fellow to LivingRoom rooms
        """
        self.lroom = livingroom.LivingRoom("Kitchen")
        self.fellow = fellow.Fellow("May", "Teresa")
        self.lroom.add_person(self.fellow)
        self.assertEqual(self.fellow, self.lroom.occupants[0])

    def test_can_add_staff_to_office_room(self):
        """
        Should be able to add staff to Office room
        """
        self.staff = staff.Staff("TT", "PP")
        self.office = office.Office("Main Office")
        self.office.add_person(self.staff)
        self.assertEqual(self.staff, self.office.occupants[0])

    def test_livingroom_raise_error_for_addition_of_staff(self):
        """
        LivingRoom should raise an InvalidRoomOccupantError exception when Staff tries to join it.
        """
        self.staff = staff.Staff("TT", "PP")
        self.lroom = livingroom.LivingRoom("Livingroom")
        with self.assertRaises(InvalidRoomOccupantError):
            self.lroom.add_person(self.staff)

    def test_can_remove_fellow_from_office(self):
        """
        Should be able to remove a fellow from office room
        """
        self.office = office.Office("Hogwarts")
        self.f1 = fellow.Fellow("Nan", "Pi")
        self.f2 = fellow.Fellow("KK", "Brown")
        self.office.add_person(self.f1)
        self.office.add_person(self.f2)

        self.assertTupleEqual(
            (self.office.remove_person(self.f2), self.office.remove_person(self.f1)),
            (self.f2, self.f1)
        )

    def test_can_remove_fellows_staff_from_office(self):
        """
        Should be able to remove Fellows and Staff from office
        """
        self.f1 = fellow.Fellow("Mark", "Mike")
        self.f2 = fellow.Fellow("JJ", "PP")
        self.s1 = staff.Staff("FF", "KK")
        self.s2 = staff.Staff("G", "FF")
        self.office = office.Office("Small Office")
        self.office.add_person(self.f1)
        self.office.add_person(self.f2)
        self.office.add_person(self.s1)
        self.office.add_person(self.s2)

        self.assertTupleEqual(
            (self.office.remove_person(self.s1), self.office.remove_person(self.s2), self.office.remove_person(self.f2),
             self.office.remove_person(self.f1),),
            (self.s1, self.s2, self.f2, self.f1)
        )

    def test_raises_exception_when_removing_non_person_type(self):
        """
        Should raise TypeError exception when a non-Person type is removed from the room
        """
        self.office = office.Office("Strange Office")
        self.fellow = fellow.Fellow("Cool", "Guy")
        with self.assertRaises(TypeError):
            self.office.remove_person('Cool Guy')


class TestAmitySystem(unittest.TestCase):
    """
    Tests for the functionality the major components of the system
    """

    def test_can_add_person_to_list(self):
        """
        Should be able to add Person to list of person
        """
        self.amity = amity.Amity()
        self.p1 = fellow.Fellow("New", "Guy")
        self.p2 = staff.Staff("New", 'Staff')
        amity.add_person(self.p1)
        amity.add_person(self.p2)
        self.assertTupleEqual(
            (self.amity.all_person[0], self.amity.all_persons[1]),
            (self.p1, self.p2)
        )

if __name__ == '__main__':
    unittest.main()
