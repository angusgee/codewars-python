import codewars_test as test
from float_precision import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution(2.34), 2.34)
        test.assert_equals(solution(5.678), 5.68)