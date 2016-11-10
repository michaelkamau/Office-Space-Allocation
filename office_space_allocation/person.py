class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def __repr__(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the Person full name
        Combination of first name and second name
        :return: full name in title case
        """
        full_name = self.first_name.strip().title() + " " + self.last_name.strip().title()
        return full_name

    # TODO: Complete definition here
