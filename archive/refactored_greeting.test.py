import codewars_test as test
from refactored_greeting import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        jack = Person("Jack")
        jill = Person("Jill")

        test.assert_equals(jack.greet("Jill"), "Hello Jill, my name is Jack")
        test.assert_equals(jack.greet("Mary"), "Hello Mary, my name is Jack")

        test.assert_equals(jill.greet("Jack"), "Hello Jack, my name is Jill")
        test.assert_equals(jill.name, 'Jill', "Person's name could not be retrieved")