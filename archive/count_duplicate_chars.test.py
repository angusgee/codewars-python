import codewars_test as test
from count_duplicate_chars import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count_duplicates(""), 0)
        test.assert_equals(count_duplicates("abcde"), 0)
        test.assert_equals(count_duplicates("abcdeaa"), 1)
        test.assert_equals(count_duplicates("abcdeaB"), 2)
        test.assert_equals(count_duplicates("Indivisibilities"), 2)