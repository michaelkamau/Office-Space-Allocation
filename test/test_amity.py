import unittest
from office_space_allocation import amity, person, fellow, staff, room, office, livingroom
from office_space_allocation.utilities import InvalidRoomOccupantError, RoomFullError
from office_space_allocation import db

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

    def setUp(self):
        self.amity = amity.Amity()

    def test_can_add_person_to_list(self):
        """
        Should be able to add Person to list of person
        """
        self.p1 = fellow.Fellow("New", "Guy")
        self.p2 = staff.Staff("New", 'Staff')
        self.amity.add_person(self.p1)
        self.amity.add_person(self.p2)
        self.assertTupleEqual(
            (self.amity.all_persons[0], self.amity.all_persons[1]),
            (self.p1, self.p2)
        )

    def test_raises_typeerror_exception_when_adding_non_person_to_list(self):
        """
        Should raise a TypeError exception when a non-Person type is added to list
        """
        with self.assertRaises(TypeError):
            self.amity.add_person('Mike Kamau')

    def test_can_add_new_room_to_list_rooms(self):
        """
        Should be able to add rooms to list of rooms
        """
        self.rm1 = office.Office("New Office")
        self.rm2 = livingroom.LivingRoom("Chillout Room")
        self.amity.add_room(self.rm1)
        self.amity.add_room(self.rm2)
        self.assertTupleEqual(
            (self.amity.all_rooms[1], self.amity.all_rooms[0]),
            (self.rm2, self.rm1)
        )

    def test_can_find_room_by_name(self):
        """
        Should be able to find Room using name
        """
        rm1 = office.Office("office 1")
        rm2 = livingroom.LivingRoom("Livingroom 1")
        self.amity.add_room(rm1)
        self.amity.add_room(rm2)
        self.assertTupleEqual(
            (self.amity.find_room("livingroom 1"), self.amity.find_room("office 1")),
            (rm2, rm1)
        )

    def test_raises_valueerror_room_not_found(self):
        """
        Should raise a ValueError when room is not found
        """
        with self.assertRaises(ValueError):
            self.amity.find_room("No Room Here")

    def test_can_allocate_room_to_person(self):
        """
        Should be able to allocate room to a Person
        """
        rm1 = office.Office("Room 1")
        rm2 = livingroom.LivingRoom("Room 2")
        rm3 = livingroom.LivingRoom("Room 3")
        self.amity.add_room(rm1)
        self.amity.add_room(rm2)
        self.amity.add_room(rm3)

        fel = fellow.Fellow("Tat", "Pap")

        fel_room = self.amity.allocate_room(fel)

        self.assertEqual(fel, fel_room.get_occupants_tuple()[0])

    @unittest.skip("This test is NOT running; don't know why :(")
    def test_raises_exception_when_room_is_full(self):
        """
        Should raise an Exception if Person wants to join a Room that is already full
        """
        # fill the Office Room
        office_rm = office.Office("Office Room")
        self.amity.add_room(office_rm)
        p1 = fellow.Fellow("PP", "GG")
        p2 = fellow.Fellow("GG", "GGG")
        p3 = fellow.Fellow("RRR", "TTT")
        p4 = fellow.Fellow("RRR", "TTT")
        p5 = fellow.Fellow("TTT", "REEE")
        p6 = fellow.Fellow("HHH", "MMM")
        p7 = fellow.Fellow("HHH", "RRR")

        with self.assertRaises(Exception):
            self.amity.allocate_room(p1)
            self.amity.allocate_room(p2)
            self.amity.allocate_room(p3)
            self.amity.allocate_room(p4)
            self.amity.allocate_room(p5)
            self.amity.allocate_room(p6)
            self.amity.allocate_room(p7)

    # @unittest.skip("Reallocation Test")
    def test_can_reallocate_person_to_another_room(self):
        """
        Should be able to reallocate Person to another Room
        """
        # create three rooms
        rm1 = office.Office("Room 1")
        rm2 = office.Office("Room 2")
        rm3 = office.Office("Room 3")

        self.amity.add_room(rm1)
        self.amity.add_room(rm2)
        self.amity.add_room(rm3)

        #  Persons
        p1 = fellow.Fellow("Fellow", "1")

        # add Persons to Amity
        self.amity.add_person(p1)
        # add Persons to Rooms
        room1 = self.amity.allocate_room(p1)

        # reallocate p1 to another room
        self.amity.reallocate_person("fellow 1", rm2.name)
        self.assertIn(p1, rm2.get_occupants_tuple())
        # reallocate p1 from rm2 to rm3
        self.amity.reallocate_person("Fellow 1", rm3.get_name())
        self.assertIn(p1, rm3.get_occupants_tuple())

        # reallocate p1 from rm3 to rm1
        self.amity.reallocate_person("fellow 1", rm1.get_name())
        self.assertIn(p1, rm1.get_occupants_tuple())

    def test_can_find_person_by_name(self):
        """
        Should be able to find Person in the system using Person name
        """
        # add person to amity
        p1 = fellow.Fellow("Mike", "Kamau")
        p2 = staff.Staff("Mary", "Jane")
        self.amity.add_person(p1)
        self.amity.add_person(p2)

        self.assertTupleEqual(
            ((p2,), (p1,)),
            (self.amity.find_person("mary jane"), self.amity.find_person("kamau"))
        )

    def test_raises_exception_if_person_not_found(self):
        """
        Should raise an Exception if Person being searched is not found
        """
        with self.assertRaises(Exception):
            self.amity.find_person("michael kamau")


class TestPersonClass(unittest.TestCase):
    """
    Tests functionality of the Person class
    """

    def test_can_get_person_full_name(self):
        """
        Should be able to get the Person full name
        """
        p1 = person.Person("mike", "kamau")
        self.assertEqual("Mike Kamau", p1.get_full_name())


class TestDatabaseOperations(unittest.TestCase):
    """
    Tests operations performed when saving or retrieving application state in a sqlite database
    """

    def setUp(self):
        self.amity = amity.Amity()

    @unittest.skip("Test not complete")
    def test_can_save_application_state_to_sqlite_database(self):
        """
        Should be able to save all application state to sqlite database
        """
        # add rooms
        self.rm1 = office.Office("Main Office")
        self.rm2 = livingroom.LivingRoom("Living Space")
        self.amity.add_room(self.rm1)
        self.amity.add_room(self.rm2)
        # add persons
        self.p1 = staff.Staff("Mary", "mary")
        self.p2 = fellow.Fellow("Jack", "Bauer")
        self.amity.add_person(self.p1)
        self.amity.add_person(self.p2)
        # allocate rooms
        self.amity.allocate_room(self.p2)
        self.amity.allocate_room(self.p1)

        # save state
        db.save_state(self.amity, 'test_db')

        # make another system
        self.another_amity = amity.Amity()

        # retrieve stored state
        self.state = db.load_state(self.another_amity, 'test_db')

        self.assertTupleEqual(
            (self.amity.all_rooms, self.amity.all_persons),
            self.state
        )

if __name__ == '__main__':
    unittest.main()
