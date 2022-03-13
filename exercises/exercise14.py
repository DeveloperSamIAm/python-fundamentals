# Lab Exercise 14 - Testing Your Code

# 11-1
import unittest
from city_functions import city_country


class CityCountryTest(unittest.TestCase):
    def test_city_country(self):
        santiago_chile = city_country("santiago", "chile")
        self.assertEqual(santiago_chile, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()


# 11-2
# run test and make sure it fails
from city_functions import city_country2


class CityCountryTest2(unittest.TestCase):
    def test_city_country2(self):
        santiago_chile = city_country2("santiago", "chile")
        self.assertEqual(santiago_chile, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()

# population parameter is optional
from city_functions import city_country3


class CityCountryTest3(unittest.TestCase):
    def test_city_country3(self):
        santiago_chile = city_country3("santiago", "chile")
        self.assertEqual(santiago_chile, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()

# write a second test called test_city_country_population() that verifies
# you can call your function with the values "santiago" "chile" and
# "population=5000000"
from city_functions import city_country4


class CityCountryTest4(unittest.TestCase):
    def test_city_country4(self):
        santiago_chile = city_country4("santiago", "chile")
        self.assertEqual(santiago_chile, "Santiago, Chile")

    def test_city_country_population(self):
        value_input = city_country4("santiago", "chile", 5_000_000)
        self.assertEqual(value_input, "Santiago, Chile - Population 5000000")


if __name__ == "__main__":
    unittest.main()


# 11-3
from city_functions import Employee


class TextEmployee(unittest.TestCase):
    def setUp(self):
        first_name = "Bob"
        last_name = "Barker"
        self.annual_salary = 50000
        self.employee = Employee(first_name, last_name, self.annual_salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, self.annual_salary + 5000)

    def test_give_custom_raise(self):
        custom_raise = 15000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.annual_salary, self.annual_salary + custom_raise)


if __name__ == "__main__":
    unittest.main()
