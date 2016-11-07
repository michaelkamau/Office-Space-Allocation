import unittest
from office_space_allocation import amity

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

if __name__ == '__main__':
    unittest.main()