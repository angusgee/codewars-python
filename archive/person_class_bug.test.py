from person_class_bug import *
import codewars_test as test

@test.describe("Basic tests")
def basic_tests():
    @test.it("Should return the person's full-name and age")
    def name_and_age():
        matz = Person('Yukihiro', 'Matsumoto', 47)
        test.assert_equals(matz.full_name, 'Yukihiro Matsumoto')
        test.assert_equals(matz.age, 47)
        
        joe = Person('Joe', 'Smith', 30)
        test.assert_equals(joe.full_name, 'Joe Smith')
        test.assert_equals(joe.age, 30)