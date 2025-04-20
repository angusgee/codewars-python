import codewars_test as test
from retrieve_arr_val_by_index_with_default import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        rng = list(range(1, 4))
        test.assert_equals(solution(rng, 1, 'a'), 2)
        test.assert_equals(solution(rng, -1, 'a'), 3)
        test.assert_equals(solution(rng, -5, 'a'), 'a')
        test.assert_equals(solution(rng, -3, 'a'), 1)

        rng = list(range(1, 6))
        test.assert_equals(solution(range(1,6), 10, 'a'), 'a')
        test.assert_equals(solution([None, None], 0, 'a'), None)

